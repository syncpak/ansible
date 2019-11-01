#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_image
description:
- Represents an Image resource.
- Google Compute Engine uses operating system images to create the root persistent
  disks for your instances. You specify an image when you create an instance. Images
  contain a boot loader, an operating system, and a root file system. Linux operating
  system images are also capable of running containers on Compute Engine.
- Images can be either public or custom.
- Public images are provided and maintained by Google, open-source communities, and
  third-party vendors. By default, all projects have access to these images and can
  use them to create instances. Custom images are available only to your project.
  You can create a custom image from root persistent disks and other images. Then,
  use the custom image to create an instance.
short_description: Creates a GCP Image
version_added: '2.6'
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
    type: str
  disk_size_gb:
    description:
    - Size of the image when restored onto a persistent disk (in GB).
    required: false
    type: int
  family:
    description:
    - The name of the image family to which this image belongs. You can create disks
      by specifying an image family instead of a specific image name. The image family
      always returns its latest image that is not deprecated. The name of the image
      family must comply with RFC1035.
    required: false
    type: str
  guest_os_features:
    description:
    - A list of features to enable on the guest operating system.
    - Applicable only for bootable images.
    required: false
    type: list
    suboptions:
      type:
        description:
        - The type of supported feature.
        - 'Some valid choices include: "MULTI_IP_SUBNET", "SECURE_BOOT", "UEFI_COMPATIBLE",
          "VIRTIO_SCSI_MULTIQUEUE", "WINDOWS"'
        required: false
        type: str
  image_encryption_key:
    description:
    - Encrypts the image using a customer-supplied encryption key.
    - After you encrypt an image with a customer-supplied key, you must provide the
      same key if you use the image later (e.g. to create a disk from the image) .
    required: false
    type: dict
    suboptions:
      raw_key:
        description:
        - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
          base64 to either encrypt or decrypt this resource.
        required: false
        type: str
  labels:
    description:
    - Labels to apply to this Image.
    required: false
    type: dict
    version_added: '2.8'
  licenses:
    description:
    - Any applicable license URI.
    required: false
    type: list
  name:
    description:
    - Name of the resource; provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  raw_disk:
    description:
    - The parameters of the raw disk image.
    required: false
    type: dict
    suboptions:
      container_type:
        description:
        - The format used to encode and transmit the block device, which should be
          TAR. This is just a container and transmission format and not a runtime
          format. Provided by the client when the disk image is created.
        - 'Some valid choices include: "TAR"'
        required: false
        type: str
      sha1_checksum:
        description:
        - An optional SHA1 checksum of the disk image before unpackaging.
        - This is provided by the client when the disk image is created.
        required: false
        type: str
      source:
        description:
        - The full Google Cloud Storage URL where disk storage is stored You must
          provide either this property or the sourceDisk property but not both.
        required: true
        type: str
  source_disk:
    description:
    - The source disk to create this image based on.
    - You must provide either this property or the rawDisk.source property but not
      both to create an image.
    - 'This field represents a link to a Disk resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_disk task and then set this source_disk field to "{{ name-of-resource
      }}"'
    required: false
    type: dict
  source_disk_encryption_key:
    description:
    - The customer-supplied encryption key of the source disk. Required if the source
      disk is protected by a customer-supplied encryption key.
    required: false
    type: dict
    suboptions:
      raw_key:
        description:
        - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
          base64 to either encrypt or decrypt this resource.
        required: false
        type: str
  source_disk_id:
    description:
    - The ID value of the disk used to create this image. This value may be used to
      determine whether the image was taken from the current or a previous instance
      of a given disk name.
    required: false
    type: str
  source_type:
    description:
    - The type of the image used to create this disk. The default and only value is
      RAW .
    - 'Some valid choices include: "RAW"'
    required: false
    type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/v1/images)'
- 'Official Documentation: U(https://cloud.google.com/compute/docs/images)'
- for authentication, you can set service_account_file using the C(gcp_service_account_file)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a disk
  gcp_compute_disk:
    name: disk-image
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: disk

- name: create a image
  gcp_compute_image:
    name: test_object
    source_disk: "{{ disk }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
archiveSizeBytes:
  description:
  - Size of the image tar.gz archive stored in Google Cloud Storage (in bytes).
  returned: success
  type: int
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
deprecated:
  description:
  - The deprecation status associated with this image.
  returned: success
  type: complex
  contains:
    deleted:
      description:
      - An optional RFC3339 timestamp on or after which the state of this resource
        is intended to change to DELETED. This is only informational and the status
        will not change unless the client explicitly changes it.
      returned: success
      type: str
    deprecated:
      description:
      - An optional RFC3339 timestamp on or after which the state of this resource
        is intended to change to DEPRECATED. This is only informational and the status
        will not change unless the client explicitly changes it.
      returned: success
      type: str
    obsolete:
      description:
      - An optional RFC3339 timestamp on or after which the state of this resource
        is intended to change to OBSOLETE. This is only informational and the status
        will not change unless the client explicitly changes it.
      returned: success
      type: str
    replacement:
      description:
      - The URL of the suggested replacement for a deprecated resource.
      - The suggested replacement resource must be the same kind of resource as the
        deprecated resource.
      returned: success
      type: str
    state:
      description:
      - The deprecation state of this resource. This can be DEPRECATED, OBSOLETE,
        or DELETED. Operations which create a new resource using a DEPRECATED resource
        will return successfully, but with a warning indicating the deprecated resource
        and recommending its replacement. Operations which use OBSOLETE or DELETED
        resources will be rejected and result in an error.
      returned: success
      type: str
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
diskSizeGb:
  description:
  - Size of the image when restored onto a persistent disk (in GB).
  returned: success
  type: int
family:
  description:
  - The name of the image family to which this image belongs. You can create disks
    by specifying an image family instead of a specific image name. The image family
    always returns its latest image that is not deprecated. The name of the image
    family must comply with RFC1035.
  returned: success
  type: str
guestOsFeatures:
  description:
  - A list of features to enable on the guest operating system.
  - Applicable only for bootable images.
  returned: success
  type: complex
  contains:
    type:
      description:
      - The type of supported feature.
      returned: success
      type: str
id:
  description:
  - The unique identifier for the resource. This identifier is defined by the server.
  returned: success
  type: int
imageEncryptionKey:
  description:
  - Encrypts the image using a customer-supplied encryption key.
  - After you encrypt an image with a customer-supplied key, you must provide the
    same key if you use the image later (e.g. to create a disk from the image) .
  returned: success
  type: complex
  contains:
    rawKey:
      description:
      - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
        base64 to either encrypt or decrypt this resource.
      returned: success
      type: str
    sha256:
      description:
      - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption
        key that protects this resource.
      returned: success
      type: str
labels:
  description:
  - Labels to apply to this Image.
  returned: success
  type: dict
labelFingerprint:
  description:
  - The fingerprint used for optimistic locking of this resource. Used internally
    during updates.
  returned: success
  type: str
licenses:
  description:
  - Any applicable license URI.
  returned: success
  type: list
name:
  description:
  - Name of the resource; provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
rawDisk:
  description:
  - The parameters of the raw disk image.
  returned: success
  type: complex
  contains:
    containerType:
      description:
      - The format used to encode and transmit the block device, which should be TAR.
        This is just a container and transmission format and not a runtime format.
        Provided by the client when the disk image is created.
      returned: success
      type: str
    sha1Checksum:
      description:
      - An optional SHA1 checksum of the disk image before unpackaging.
      - This is provided by the client when the disk image is created.
      returned: success
      type: str
    source:
      description:
      - The full Google Cloud Storage URL where disk storage is stored You must provide
        either this property or the sourceDisk property but not both.
      returned: success
      type: str
sourceDisk:
  description:
  - The source disk to create this image based on.
  - You must provide either this property or the rawDisk.source property but not both
    to create an image.
  returned: success
  type: dict
sourceDiskEncryptionKey:
  description:
  - The customer-supplied encryption key of the source disk. Required if the source
    disk is protected by a customer-supplied encryption key.
  returned: success
  type: complex
  contains:
    rawKey:
      description:
      - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
        base64 to either encrypt or decrypt this resource.
      returned: success
      type: str
    sha256:
      description:
      - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption
        key that protects this resource.
      returned: success
      type: str
sourceDiskId:
  description:
  - The ID value of the disk used to create this image. This value may be used to
    determine whether the image was taken from the current or a previous instance
    of a given disk name.
  returned: success
  type: str
sourceType:
  description:
  - The type of the image used to create this disk. The default and only value is
    RAW .
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            disk_size_gb=dict(type='int'),
            family=dict(type='str'),
            guest_os_features=dict(type='list', elements='dict', options=dict(type=dict(type='str'))),
            image_encryption_key=dict(type='dict', options=dict(raw_key=dict(type='str'))),
            labels=dict(type='dict'),
            licenses=dict(type='list', elements='str'),
            name=dict(required=True, type='str'),
            raw_disk=dict(type='dict', options=dict(container_type=dict(type='str'), sha1_checksum=dict(type='str'), source=dict(required=True, type='str'))),
            source_disk=dict(type='dict'),
            source_disk_encryption_key=dict(type='dict', options=dict(raw_key=dict(type='str'))),
            source_disk_id=dict(type='str'),
            source_type=dict(type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#image'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if response.get('labels') != request.get('labels'):
        labels_update(module, request, response)


def labels_update(module, request, response):
    auth = GcpSession(module, 'compute')
    auth.post(
        ''.join(["https://www.googleapis.com/compute/v1/", "projects/{project}/global/images/{name}/setLabels"]).format(**module.params),
        {u'labels': module.params.get('labels'), u'labelFingerprint': response.get('labelFingerprint')},
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#image',
        u'description': module.params.get('description'),
        u'diskSizeGb': module.params.get('disk_size_gb'),
        u'family': module.params.get('family'),
        u'guestOsFeatures': ImageGuestosfeaturesArray(module.params.get('guest_os_features', []), module).to_request(),
        u'imageEncryptionKey': ImageImageencryptionkey(module.params.get('image_encryption_key', {}), module).to_request(),
        u'labels': module.params.get('labels'),
        u'licenses': module.params.get('licenses'),
        u'name': module.params.get('name'),
        u'rawDisk': ImageRawdisk(module.params.get('raw_disk', {}), module).to_request(),
        u'sourceDisk': replace_resource_dict(module.params.get(u'source_disk', {}), 'selfLink'),
        u'sourceDiskEncryptionKey': ImageSourcediskencryptionkey(module.params.get('source_disk_encryption_key', {}), module).to_request(),
        u'sourceDiskId': module.params.get('source_disk_id'),
        u'sourceType': module.params.get('source_type'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/images/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/images".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'archiveSizeBytes': response.get(u'archiveSizeBytes'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'deprecated': ImageDeprecated(response.get(u'deprecated', {}), module).from_response(),
        u'description': response.get(u'description'),
        u'diskSizeGb': response.get(u'diskSizeGb'),
        u'family': response.get(u'family'),
        u'guestOsFeatures': ImageGuestosfeaturesArray(response.get(u'guestOsFeatures', []), module).from_response(),
        u'id': response.get(u'id'),
        u'imageEncryptionKey': ImageImageencryptionkey(response.get(u'imageEncryptionKey', {}), module).from_response(),
        u'labels': response.get(u'labels'),
        u'labelFingerprint': response.get(u'labelFingerprint'),
        u'licenses': response.get(u'licenses'),
        u'name': response.get(u'name'),
        u'rawDisk': ImageRawdisk(response.get(u'rawDisk', {}), module).from_response(),
        u'sourceDisk': response.get(u'sourceDisk'),
        u'sourceDiskEncryptionKey': ImageSourcediskencryptionkey(response.get(u'sourceDiskEncryptionKey', {}), module).from_response(),
        u'sourceDiskId': response.get(u'sourceDiskId'),
        u'sourceType': response.get(u'sourceType'),
    }


def license_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1//projects/.*/global/licenses/.*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1//projects/{project}/global/licenses/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#image')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class ImageDeprecated(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'deleted': self.request.get('deleted'),
                u'deprecated': self.request.get('deprecated'),
                u'obsolete': self.request.get('obsolete'),
                u'replacement': self.request.get('replacement'),
                u'state': self.request.get('state'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'deleted': self.request.get(u'deleted'),
                u'deprecated': self.request.get(u'deprecated'),
                u'obsolete': self.request.get(u'obsolete'),
                u'replacement': self.request.get(u'replacement'),
                u'state': self.request.get(u'state'),
            }
        )


class ImageGuestosfeaturesArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({u'type': item.get('type')})

    def _response_from_item(self, item):
        return remove_nones_from_dict({u'type': item.get(u'type')})


class ImageImageencryptionkey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'rawKey': self.request.get('raw_key')})

    def from_response(self):
        return remove_nones_from_dict({u'rawKey': self.request.get(u'rawKey')})


class ImageRawdisk(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'containerType': self.request.get('container_type'), u'sha1Checksum': self.request.get('sha1_checksum'), u'source': self.request.get('source')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'containerType': self.request.get(u'containerType'), u'sha1Checksum': self.request.get(u'sha1Checksum'), u'source': self.request.get(u'source')}
        )


class ImageSourcediskencryptionkey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({u'rawKey': self.request.get('raw_key')})

    def from_response(self):
        return remove_nones_from_dict({u'rawKey': self.request.get(u'rawKey')})


if __name__ == '__main__':
    main()
