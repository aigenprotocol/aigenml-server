import os.path

from aigenml import save_model_create_shards
from flask import request, jsonify
from rq.job import Job

from server.models import AIProject
from server.utils import save_files, slugify
from .globals import globals as g


@g.app.route("/")
def home():
    return {"status": "success", "message": "Hello, World"}


@g.app.route("/project/shards", methods=["get", "post"])
def create_project_shards():
    if request.method == 'POST':
        project_id = request.form.get('project_id', None)
        project_name = request.form.get('project_name', None)
        no_of_ainfts = request.form.get('no_of_ainfts', None)

        if project_id is None or project_name is None or no_of_ainfts is None:
            return {"status": "failure",
                    "message": "Required values are missing"}

        project_name = slugify(project_name)
        project_name1 = f"{slugify(project_name)}_{project_id}"
        project_dir = os.path.join(g.app.config['PROJECTS_DIR'], project_name1)
        response = save_files(request)
        if response['status'] == "success":
            job = g.q.enqueue(save_model_create_shards, project_name=project_name, project_id=project_id,
                              project_dir=project_dir,
                              model_path=response['model_file_path'], no_of_ainfts=int(no_of_ainfts))

            # create project if not exists
            projects = AIProject.query.filter_by(id=project_id).all()
            if len(projects) == 0:
                project = AIProject(id=project_id, name=project_name,
                                    model_dir=project_dir,
                                    no_of_ainfts=int(no_of_ainfts), progress=0, job_id=job.id,
                                    status="Created")
                g.db.session.add(project)
                g.db.session.commit()
            else:
                project = projects[0]
                project.model_dir = project_dir
                project.no_of_ainfts = int(no_of_ainfts)
                project.job_id = job.id

                # Commit the changes to the database
                g.db.session.commit()

            return jsonify({"status": "success",
                            "message": "Job started: Model extraction and shards creation"})
        else:
            return response
    else:
        return jsonify({"status": "failure", "message": "Invalid request"})


@g.app.route("/project/job/status", methods=["get"])
def get_project_job_status():
    if request.method == 'GET':
        project_id = request.args.get("project_id", None)

        if project_id is None:
            return {"status": "failure",
                    "message": "Project id is missing"}

        projects = AIProject.query.filter_by(id=project_id).all()
        if len(projects) > 0:
            project = projects[0]
            job_id = project.job_id

            return jsonify({"status": "success", "job_status": Job.fetch(job_id, g.r).get_status()})
        else:
            return jsonify({"status": "failure", "message": "Invalid project id"})
    else:
        return jsonify({"status": "failure", "message": "Invalid request"})
