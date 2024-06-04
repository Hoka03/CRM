def normalize_text(obj):
    for i in obj.get_normalize_fields():
        fields = getattr(obj, i)
        setattr(obj, i, ' '.join(fields.split()))