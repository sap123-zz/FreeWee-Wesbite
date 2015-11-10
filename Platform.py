import os

if 'OPENSHIFT_APP_DNS' in os.environ:
    IS_OPENSHIFT = True
else:
    IS_OPENSHIFT = False

