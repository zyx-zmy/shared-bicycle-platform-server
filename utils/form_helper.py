
def verify_form(form_class, data):
    form = form_class(data)
    if form.is_valid():
        return form.cleaned_data, True
    errors = []
    for k, v in form.errors.items():
        if v.get_json_data()[0]['code'] == 'required':
            errors.append({'field': k,'code': 'missing_field'})
        else:
            errors.append({'field': k, 'code': 'invalid'})
    return {'errors': errors}, False