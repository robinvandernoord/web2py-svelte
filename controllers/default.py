# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
@svelte()
def index():
    response.flash = 'This still works too!'
    return {'name': 'backend'}


@svelte('Alternate')
def page2():
    return {'nested_data': {'nest 1': {'id': 1, 'value': 35, 'deeper': {'boolean': True}},
                            'nest 2': {'id': 2, 'value': 12, 'deeper': {'boolean': False}},
                            'nest 3': {'id': 3, 'value': 64, 'deeper': {'boolean': None}},
                            }}


def non_svelte():
    return {}


# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
