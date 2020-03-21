"""
module for testing qualys_cloud_agent
"""
import logging
import pytest
import testinfra


@pytest.mark.qualys_cloud_agent
class TestQualys:
    """
    Test class for qualys_cloud_agent install
    """

    @pytest.mark.qualys_cloud_agent_package
    def test_package(self, host, load_defaults, load_overrides):
        """
        test if package is installed
        """
        module_vars = {**load_defaults, **load_overrides}
        package = host.package(module_vars['qualys_cloud_agent_package_name'])
        pytest.assume(package.is_installed)
        if module_vars['qualys_cloud_agent_package_version']:
            pytest.assume(package.version == module_vars['qualys_cloud_agent_package_version'])

    @pytest.mark.qualys_cloud_agent_service
    def test_service(self, host, load_defaults, load_overrides):
        """
        test if service is configured correctly
        """
        module_vars = {**load_defaults, **load_overrides}
        service = host.service(module_vars['qualys_cloud_agent_service_name'])
        # only check service is not performing a build
        if module_vars['qualys_cloud_agent_build']:
            pytest.assume(service.is_enabled == module_vars['qualys_cloud_agent_service_enabled'])
            pytest.assume(service.is_running == false)
            return
        # test service is in correct state
        if module_vars['qualys_cloud_agent_service_enabled']:
            pytest.assume(service.is_enabled == module_vars['qualys_cloud_agent_service_enabled'])
        if module_vars['qualys_cloud_agent_service_running']:
            pytest.assume(service.is_running == module_vars['qualys_cloud_agent_service_running'])

    @pytest.mark.qualys_cloud_agent_process
    def test_process(self, host, load_defaults, load_overrides):
        """
        test process is running correctly
        """
        module_vars = {**load_defaults, **load_overrides}
        process = host.process.get(comm=module_vars['qualys_cloud_agent_service_process'])
        if module_vars['qualys_cloud_agent_build']:
            # ensure process is not running
            pytest.assume(process is None)
        else:
            pytest.assume(process.pid is not None)

    @pytest.mark.qualys_cloud_agent_config_file
    def test_config_file(self, host, load_defaults, load_overrides):
        """
        test if configuration file configured correctly
        """
        module_vars = {**load_defaults, **load_overrides}
        config_file = host.file(module_vars['qualys_cloud_agent_config_path'])
        pytest.assume(config_file.exists)
        pytest.assume(config_file.user == module_vars['qualys_cloud_agent_config_path_user'])
        pytest.assume(config_file.group == module_vars['qualys_cloud_agent_config_path_group'])
        pytest.assume(oct(config_file.mode)[-3:] == module_vars['qualys_cloud_agent_config_path_mode'])
        if module_vars['qualys_cloud_agent_config_ActivationId']:
            pytest.assume(config_file.contains("ActivationId *= *'{}'".format(module_vars['qualys_cloud_agent_config_ActivationId'])))
        if module_vars['qualys_cloud_agent_config_CustomerId']:
            pytest.assume(config_file.contains("CustomerId *= *'{}'".format(module_vars['qualys_cloud_agent_config_CustomerId'])))
        if module_vars['qualys_cloud_agent_config_LogLevel']:
            pytest.assume(config_file.contains("LogLevel *= *'{}'".format(module_vars['qualys_cloud_agent_config_LogLevel'])))
        if module_vars['qualys_cloud_agent_config_LogFileDir']:
            pytest.assume(config_file.contains("LogFileDir *= *'{}'".format(module_vars['qualys_cloud_agent_config_LogFileDir'])))
        if module_vars['qualys_cloud_agent_config_UseSudo']:
            pytest.assume(config_file.contains("UseSudo *= *'{}'".format(module_vars['qualys_cloud_agent_config_UseSudo'])))
        if module_vars['qualys_cloud_agent_config_User']:
            pytest.assume(config_file.contains("User *= *'{}'".format(module_vars['qualys_cloud_agent_config_User'])))
        if module_vars['qualys_cloud_agent_config_Group']:
            pytest.assume(config_file.contains("Group *= *'{}'".format(module_vars['qualys_cloud_agent_config_Group'])))
        if module_vars['qualys_cloud_agent_config_HostIdSearchDir']:
            pytest.assume(config_file.contains("HostIdSearchDir *= *'{}'".format(module_vars['qualys_cloud_agent_config_HostIdSearchDir'])))
        if module_vars['qualys_cloud_agent_config_LogDestType']:
            pytest.assume(config_file.contains("LogDestType *= *'{}'".format(module_vars['qualys_cloud_agent_config_LogDestType'])))
        if module_vars['qualys_cloud_agent_config_ServerUri']:
            pytest.assume(config_file.contains("ServerUri *= *'{}'".format(module_vars['qualys_cloud_agent_config_ServerUri'])))
        if module_vars['qualys_cloud_agent_config_CmdMaxTimeOut']:
            pytest.assume(config_file.contains("CmdMaxTimeOut *= *'{}'".format(module_vars['qualys_cloud_agent_config_CmdMaxTimeOut'])))
        if module_vars['qualys_cloud_agent_config_ProcessPriority']:
            pytest.assume(config_file.contains("ProcessPriority *= *'{}'".format(module_vars['qualys_cloud_agent_config_ProcessPriority'])))
        if module_vars['qualys_cloud_agent_config_UseAuditDispatcher']:
            pytest.assume(config_file.contains("UseAuditDispatcher *= *'{}'".format(module_vars['qualys_cloud_agent_config_UseAuditDispatcher'])))
