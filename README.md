# testinfra-qualys-cloud-agent
Testinfra pytest for qualys-cloud-agent.

## Installation
```
python -m venv venv
source venv/bin/activate
pip install -r requirements_install.txt
```
Create a python virtual environment.
Activate and install requirements.
Now ready to run tests.
## Pytest Run
```
pytest -vs
```

## Pytest Markers
* qualys_cloud_agent: qualys_cloud_agent all tests from class
* qualys_cloud_agent_package: qualys_cloud_agent install tests
* qualys_cloud_agent_service: qualys_cloud_agent service tests
* qualys_cloud_agent_process: qualys_cloud_agent service tests
* qualys_cloud_agent_config_file: qualys_cloud_agent config tests

## Qualys_cloud_agent default variables
Contains a yaml list of all default values.
Fixture to return default values qualys_cloud_agent/conftest.py

### qualys_cloud_agent/defaults/main.yml
* qualys_cloud_agent_build - sets whether or not to test if this is a build for a "golden image"
    * If this is a golden ami the service and process should not be running but set to the desired <span style="color: grey">qualys_cloud_agent_service_enabled</span> value

## Qualys_cloud_agent override variables
* overrides/main.yml
Contains a yaml list of all override values that are merged into default
dictionary.
Fixture to return overrides conftest.py
