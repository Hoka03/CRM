def student_photo_upload_path(obj, image):
    if obj.role == 'student':
        return f'groups/{obj.student_group.subject.name}/{obj.first_name}/photos/{image}'
    return f'groups/{image}'