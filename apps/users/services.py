def student_photo_upload_path(obj, image):
    return f'groups/{obj.student_group.subject.name}/{obj.first_name}/photos/{image}'
