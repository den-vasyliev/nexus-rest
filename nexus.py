"""v.1402-1550 denys.vasyliev@qsc.com
Simply REST API Module for Nexus Repository ManagerOSS 3.8.0-0

Please find more on swagger http://<nexus_hostname>/#admin/system/api

Quick Start:
Import Module: import nexus
Credentials: nexus.nexusConfig={'host':'localhost:8081','credentials':['admin','admin123']}
Upload: nexus.upload('builds','test','1','nexus.py') # Return 201
Search: nexus.search({'q':'nexus.py'}) # Return assets in JSON
Delete: nexus.assets_del('YnVpbGRzOjkzYjliOWViOWE3ZWNiMDZiNTY5OTYyZGEyZDNhNTc5') # Return 204

"""
import requests

nexusConfig = {}


def _run(cmd, opt='get'):

    assert nexusConfig.get('host') is not None, "host not defined"
    assert nexusConfig.get('credentials') is not None, "credentials not defined"

    headers = {'Accept': 'application/json'}
    url = 'http://%s/service/rest/beta/%s' % (nexusConfig['host'], cmd)

    if opt == 'get':
        result = requests.get(url, headers=headers, auth=(nexusConfig['credentials'][0], nexusConfig['credentials'][1]))
    elif opt == 'delete':
        result = requests.delete(url, headers=headers,
                                 auth=(nexusConfig['credentials'][0], nexusConfig['credentials'][1]))
    else:
        url = 'http://%s/repository/%s' % (nexusConfig['host'], cmd)
        files = open(opt, 'rb')
        result = requests.put(url, data=files, auth=(nexusConfig['credentials'][0], nexusConfig['credentials'][1]))

    return result.status_code, result.text


def upload(repo, branch_name, build_name, file_name):
    """Upload file to RAW repository
  201 Created"""
    cmd = "%s/%s/%s/%s" % (repo, branch_name, build_name, file_name)
    return _run(cmd, file_name)


def assets_get(repository):
    """<REPOSITORY> from which you would like to retrieve assets"""
    cmd = "assets?repository=%s" % repository
    return _run(cmd)


def assets_del(asset_id):
    """<ID> of the asset to delete
  204 Component was successfully deleted
  403 Insufficient permissions to delete component
  404 Component not found
  422 Malformed ID"""
    cmd = "assets/%s" % asset_id
    return _run(cmd, 'delete')


def assets_get_id(asset_id):
    """GET <ID> of the asset to get"""
    cmd = "assets/%s" % asset_id
    return _run(cmd)


def components_get(repository):
    """<REPOSITORY>  from which you would like to retrieve components
  204 Component was successfully deleted
  403 Insufficient permissions to delete component
  404 Component not found
  422 Malformed ID"""
    cmd = "components?repository=%s" % repository
    return _run(cmd)


def components_del(component_id):
    """<ID> of the component to delete"""
    cmd = "components/%s" % component_id
    return _run(cmd, 'delete')


def components_get_id(component_id):
    """<ID> of the component to retrieve"""
    cmd = "components/%s" % (component_id)
    return _run(cmd)


def readonly():
    """Not implemented yet"""
    # get
    # post
    # post
    # post
    return 'Not implemented yet'


def script():
    """Not implemented yet"""
    # get
    # post
    # delete
    # get
    # put
    # post
    return 'Not implemented yet'


def search(query):
    """Query by param and keyword
query is a dict 'param':'keyword'
Param in:
q|repository|format|group|name|version|
md5|sha1|sha256|sha512|
docker.imageName|docker.imageTag|docker.layerId|docker.contentDigest|
maven.groupId|maven.artifactId|maven.baseVersion|maven.extension|maven.classifier|
npm.scope|nuget.id|nuget.tags|
pypi.classifiers|pypi.description|pypi.keywords|pypi.summary|
rubygems.description|rubygems.platform|rubygems.summary|yum.architecture

Example:
query={'q':'qlmm-mvp-1802', 'repository':'builds'}
nexus.search(nexusConfig, query)
  """
    query_ = ''
    for k, v in sorted(query.items()):
        query_ = '%s&%s=%s' % (query_, k, v)
    cmd = "search?%s" % query_
    return _run(cmd)


def search_assets(query):
    """Query by keyword"""
    query_ = ''
    for k, v in sorted(query.items()):
        query_ = '%s&%s=%s' % (query_, k, v)
    cmd = "search?%s" % query_
    return _run(cmd)


# GET /beta/search/assets
def search_download(query):
    """Query by keyword"""
    cmd = "search/assets/download?q=%s" % (query)
    return _run(cmd)


# GET /beta/search/assets/download
# Returns a 302 Found with location header field set to download URL. Search must return a single asset to
# receive download URL.

def tasks():
    """Not implemented yet"""
    return 'Not implemented yet'
# get
# get
# post
# post

