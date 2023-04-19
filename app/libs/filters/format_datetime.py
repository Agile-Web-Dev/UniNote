from flask import current_app as app


@app.template_filter('format_datetime')
def datetime_filter(t):
    print(t)
    return t.strftime('%m/%d/%Y, %H:%M:%S')
