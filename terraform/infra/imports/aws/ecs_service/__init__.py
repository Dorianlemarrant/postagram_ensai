r'''
# `aws_ecs_service`

Refer to the Terraform Registry for docs: [`aws_ecs_service`](https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class EcsService(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsService",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service aws_ecs_service}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        alarms: typing.Optional[typing.Union["EcsServiceAlarms", typing.Dict[builtins.str, typing.Any]]] = None,
        availability_zone_rebalancing: typing.Optional[builtins.str] = None,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_connect_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume_configuration: typing.Optional[typing.Union["EcsServiceVolumeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_lattice_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceVpcLatticeConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service aws_ecs_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.
        :param alarms: alarms block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarms EcsService#alarms}
        :param availability_zone_rebalancing: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#availability_zone_rebalancing EcsService#availability_zone_rebalancing}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_delete EcsService#force_delete}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_connect_configuration: service_connect_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#timeouts EcsService#timeouts}
        :param triggers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#triggers EcsService#triggers}.
        :param volume_configuration: volume_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_configuration EcsService#volume_configuration}
        :param vpc_lattice_configurations: vpc_lattice_configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#vpc_lattice_configurations EcsService#vpc_lattice_configurations}
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37ac4570462af646dff8e915110fdf704bcbbf8a668ca7b90381d776cd581665)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EcsServiceConfig(
            name=name,
            alarms=alarms,
            availability_zone_rebalancing=availability_zone_rebalancing,
            capacity_provider_strategy=capacity_provider_strategy,
            cluster=cluster,
            deployment_circuit_breaker=deployment_circuit_breaker,
            deployment_controller=deployment_controller,
            deployment_maximum_percent=deployment_maximum_percent,
            deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
            desired_count=desired_count,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            force_delete=force_delete,
            force_new_deployment=force_new_deployment,
            health_check_grace_period_seconds=health_check_grace_period_seconds,
            iam_role=iam_role,
            id=id,
            launch_type=launch_type,
            load_balancer=load_balancer,
            network_configuration=network_configuration,
            ordered_placement_strategy=ordered_placement_strategy,
            placement_constraints=placement_constraints,
            platform_version=platform_version,
            propagate_tags=propagate_tags,
            scheduling_strategy=scheduling_strategy,
            service_connect_configuration=service_connect_configuration,
            service_registries=service_registries,
            tags=tags,
            tags_all=tags_all,
            task_definition=task_definition,
            timeouts=timeouts,
            triggers=triggers,
            volume_configuration=volume_configuration,
            vpc_lattice_configurations=vpc_lattice_configurations,
            wait_for_steady_state=wait_for_steady_state,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a EcsService resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the EcsService to import.
        :param import_from_id: The id of the existing EcsService that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the EcsService to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ed5de39cce407e6330cc852669606c2b7683017f4544f0ba9c7d12c35ea7a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAlarms")
    def put_alarms(
        self,
        *,
        alarm_names: typing.Sequence[builtins.str],
        enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param alarm_names: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarm_names EcsService#alarm_names}.
        :param enable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.
        '''
        value = EcsServiceAlarms(
            alarm_names=alarm_names, enable=enable, rollback=rollback
        )

        return typing.cast(None, jsii.invoke(self, "putAlarms", [value]))

    @jsii.member(jsii_name="putCapacityProviderStrategy")
    def put_capacity_provider_strategy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceCapacityProviderStrategy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37cfccd18c498c53efcdb2611369b975d39b610f485b4d317f36633aa7909b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCapacityProviderStrategy", [value]))

    @jsii.member(jsii_name="putDeploymentCircuitBreaker")
    def put_deployment_circuit_breaker(
        self,
        *,
        enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.
        '''
        value = EcsServiceDeploymentCircuitBreaker(enable=enable, rollback=rollback)

        return typing.cast(None, jsii.invoke(self, "putDeploymentCircuitBreaker", [value]))

    @jsii.member(jsii_name="putDeploymentController")
    def put_deployment_controller(
        self,
        *,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.
        '''
        value = EcsServiceDeploymentController(type=type)

        return typing.cast(None, jsii.invoke(self, "putDeploymentController", [value]))

    @jsii.member(jsii_name="putLoadBalancer")
    def put_load_balancer(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c449529175f15b84c519472c936cf5ba5349e9e7c704bd92ecae94bac26e29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLoadBalancer", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#security_groups EcsService#security_groups}.
        '''
        value = EcsServiceNetworkConfiguration(
            subnets=subnets,
            assign_public_ip=assign_public_ip,
            security_groups=security_groups,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putOrderedPlacementStrategy")
    def put_ordered_placement_strategy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea64e0b414c090e191490c9feef9e16231a98148e80fa8f2f27bc2da9f8c07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOrderedPlacementStrategy", [value]))

    @jsii.member(jsii_name="putPlacementConstraints")
    def put_placement_constraints(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb1b694c4aba723ecac977a43c9021e5d74d164d31da946e8e006da012a2e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlacementConstraints", [value]))

    @jsii.member(jsii_name="putServiceConnectConfiguration")
    def put_service_connect_configuration(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        log_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationLogConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationService", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enabled EcsService#enabled}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_configuration EcsService#log_configuration}
        :param namespace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#namespace EcsService#namespace}.
        :param service: service block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service EcsService#service}
        '''
        value = EcsServiceServiceConnectConfiguration(
            enabled=enabled,
            log_configuration=log_configuration,
            namespace=namespace,
            service=service,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceConnectConfiguration", [value]))

    @jsii.member(jsii_name="putServiceRegistries")
    def put_service_registries(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.
        '''
        value = EcsServiceServiceRegistries(
            registry_arn=registry_arn,
            container_name=container_name,
            container_port=container_port,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putServiceRegistries", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#update EcsService#update}.
        '''
        value = EcsServiceTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVolumeConfiguration")
    def put_volume_configuration(
        self,
        *,
        managed_ebs_volume: typing.Union["EcsServiceVolumeConfigurationManagedEbsVolume", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
    ) -> None:
        '''
        :param managed_ebs_volume: managed_ebs_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#managed_ebs_volume EcsService#managed_ebs_volume}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.
        '''
        value = EcsServiceVolumeConfiguration(
            managed_ebs_volume=managed_ebs_volume, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putVolumeConfiguration", [value]))

    @jsii.member(jsii_name="putVpcLatticeConfigurations")
    def put_vpc_lattice_configurations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceVpcLatticeConfigurations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a263d883acebe332c84ff454abcc5bd48c8595b25c44190f2bd8c4d741ea5a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVpcLatticeConfigurations", [value]))

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @jsii.member(jsii_name="resetAvailabilityZoneRebalancing")
    def reset_availability_zone_rebalancing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZoneRebalancing", []))

    @jsii.member(jsii_name="resetCapacityProviderStrategy")
    def reset_capacity_provider_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityProviderStrategy", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetDeploymentCircuitBreaker")
    def reset_deployment_circuit_breaker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentCircuitBreaker", []))

    @jsii.member(jsii_name="resetDeploymentController")
    def reset_deployment_controller(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentController", []))

    @jsii.member(jsii_name="resetDeploymentMaximumPercent")
    def reset_deployment_maximum_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMaximumPercent", []))

    @jsii.member(jsii_name="resetDeploymentMinimumHealthyPercent")
    def reset_deployment_minimum_healthy_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMinimumHealthyPercent", []))

    @jsii.member(jsii_name="resetDesiredCount")
    def reset_desired_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDesiredCount", []))

    @jsii.member(jsii_name="resetEnableEcsManagedTags")
    def reset_enable_ecs_managed_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableEcsManagedTags", []))

    @jsii.member(jsii_name="resetEnableExecuteCommand")
    def reset_enable_execute_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableExecuteCommand", []))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetForceNewDeployment")
    def reset_force_new_deployment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceNewDeployment", []))

    @jsii.member(jsii_name="resetHealthCheckGracePeriodSeconds")
    def reset_health_check_grace_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckGracePeriodSeconds", []))

    @jsii.member(jsii_name="resetIamRole")
    def reset_iam_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRole", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaunchType")
    def reset_launch_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaunchType", []))

    @jsii.member(jsii_name="resetLoadBalancer")
    def reset_load_balancer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancer", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetOrderedPlacementStrategy")
    def reset_ordered_placement_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderedPlacementStrategy", []))

    @jsii.member(jsii_name="resetPlacementConstraints")
    def reset_placement_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacementConstraints", []))

    @jsii.member(jsii_name="resetPlatformVersion")
    def reset_platform_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformVersion", []))

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetSchedulingStrategy")
    def reset_scheduling_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedulingStrategy", []))

    @jsii.member(jsii_name="resetServiceConnectConfiguration")
    def reset_service_connect_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceConnectConfiguration", []))

    @jsii.member(jsii_name="resetServiceRegistries")
    def reset_service_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceRegistries", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTaskDefinition")
    def reset_task_definition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskDefinition", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTriggers")
    def reset_triggers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggers", []))

    @jsii.member(jsii_name="resetVolumeConfiguration")
    def reset_volume_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeConfiguration", []))

    @jsii.member(jsii_name="resetVpcLatticeConfigurations")
    def reset_vpc_lattice_configurations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcLatticeConfigurations", []))

    @jsii.member(jsii_name="resetWaitForSteadyState")
    def reset_wait_for_steady_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForSteadyState", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> "EcsServiceAlarmsOutputReference":
        return typing.cast("EcsServiceAlarmsOutputReference", jsii.get(self, "alarms"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategy")
    def capacity_provider_strategy(self) -> "EcsServiceCapacityProviderStrategyList":
        return typing.cast("EcsServiceCapacityProviderStrategyList", jsii.get(self, "capacityProviderStrategy"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreaker")
    def deployment_circuit_breaker(
        self,
    ) -> "EcsServiceDeploymentCircuitBreakerOutputReference":
        return typing.cast("EcsServiceDeploymentCircuitBreakerOutputReference", jsii.get(self, "deploymentCircuitBreaker"))

    @builtins.property
    @jsii.member(jsii_name="deploymentController")
    def deployment_controller(self) -> "EcsServiceDeploymentControllerOutputReference":
        return typing.cast("EcsServiceDeploymentControllerOutputReference", jsii.get(self, "deploymentController"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> "EcsServiceLoadBalancerList":
        return typing.cast("EcsServiceLoadBalancerList", jsii.get(self, "loadBalancer"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "EcsServiceNetworkConfigurationOutputReference":
        return typing.cast("EcsServiceNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategy")
    def ordered_placement_strategy(self) -> "EcsServiceOrderedPlacementStrategyList":
        return typing.cast("EcsServiceOrderedPlacementStrategyList", jsii.get(self, "orderedPlacementStrategy"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraints")
    def placement_constraints(self) -> "EcsServicePlacementConstraintsList":
        return typing.cast("EcsServicePlacementConstraintsList", jsii.get(self, "placementConstraints"))

    @builtins.property
    @jsii.member(jsii_name="serviceConnectConfiguration")
    def service_connect_configuration(
        self,
    ) -> "EcsServiceServiceConnectConfigurationOutputReference":
        return typing.cast("EcsServiceServiceConnectConfigurationOutputReference", jsii.get(self, "serviceConnectConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistries")
    def service_registries(self) -> "EcsServiceServiceRegistriesOutputReference":
        return typing.cast("EcsServiceServiceRegistriesOutputReference", jsii.get(self, "serviceRegistries"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "EcsServiceTimeoutsOutputReference":
        return typing.cast("EcsServiceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="volumeConfiguration")
    def volume_configuration(self) -> "EcsServiceVolumeConfigurationOutputReference":
        return typing.cast("EcsServiceVolumeConfigurationOutputReference", jsii.get(self, "volumeConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="vpcLatticeConfigurations")
    def vpc_lattice_configurations(self) -> "EcsServiceVpcLatticeConfigurationsList":
        return typing.cast("EcsServiceVpcLatticeConfigurationsList", jsii.get(self, "vpcLatticeConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(self) -> typing.Optional["EcsServiceAlarms"]:
        return typing.cast(typing.Optional["EcsServiceAlarms"], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRebalancingInput")
    def availability_zone_rebalancing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZoneRebalancingInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderStrategyInput")
    def capacity_provider_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceCapacityProviderStrategy"]]], jsii.get(self, "capacityProviderStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentCircuitBreakerInput")
    def deployment_circuit_breaker_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], jsii.get(self, "deploymentCircuitBreakerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentControllerInput")
    def deployment_controller_input(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], jsii.get(self, "deploymentControllerInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercentInput")
    def deployment_maximum_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMaximumPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercentInput")
    def deployment_minimum_healthy_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "deploymentMinimumHealthyPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredCountInput")
    def desired_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredCountInput"))

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTagsInput")
    def enable_ecs_managed_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableEcsManagedTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommandInput")
    def enable_execute_command_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableExecuteCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="forceNewDeploymentInput")
    def force_new_deployment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceNewDeploymentInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSecondsInput")
    def health_check_grace_period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthCheckGracePeriodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleInput")
    def iam_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="launchTypeInput")
    def launch_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "launchTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInput")
    def load_balancer_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceLoadBalancer"]]], jsii.get(self, "loadBalancerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="orderedPlacementStrategyInput")
    def ordered_placement_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], jsii.get(self, "orderedPlacementStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="placementConstraintsInput")
    def placement_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServicePlacementConstraints"]]], jsii.get(self, "placementConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="platformVersionInput")
    def platform_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategyInput")
    def scheduling_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceConnectConfigurationInput")
    def service_connect_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfiguration"], jsii.get(self, "serviceConnectConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRegistriesInput")
    def service_registries_input(
        self,
    ) -> typing.Optional["EcsServiceServiceRegistries"]:
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], jsii.get(self, "serviceRegistriesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionInput")
    def task_definition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskDefinitionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "EcsServiceTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "EcsServiceTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggersInput")
    def triggers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "triggersInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeConfigurationInput")
    def volume_configuration_input(
        self,
    ) -> typing.Optional["EcsServiceVolumeConfiguration"]:
        return typing.cast(typing.Optional["EcsServiceVolumeConfiguration"], jsii.get(self, "volumeConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcLatticeConfigurationsInput")
    def vpc_lattice_configurations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVpcLatticeConfigurations"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVpcLatticeConfigurations"]]], jsii.get(self, "vpcLatticeConfigurationsInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyStateInput")
    def wait_for_steady_state_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForSteadyStateInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneRebalancing")
    def availability_zone_rebalancing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityZoneRebalancing"))

    @availability_zone_rebalancing.setter
    def availability_zone_rebalancing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33305a2f2c8ca9caa8f36c801cadc950a272351dc4f7b8b1cb708587bcfafcad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneRebalancing", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cluster"))

    @cluster.setter
    def cluster(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a2049343789f7180c210b28c083910dfb0a5ff1e951feca6f301fb0f925e5be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cluster", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deploymentMaximumPercent")
    def deployment_maximum_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMaximumPercent"))

    @deployment_maximum_percent.setter
    def deployment_maximum_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da20988d2dd298506a27c1aa51fdf24775ba02724bea0a5962772ca96825cbd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMaximumPercent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deploymentMinimumHealthyPercent")
    def deployment_minimum_healthy_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "deploymentMinimumHealthyPercent"))

    @deployment_minimum_healthy_percent.setter
    def deployment_minimum_healthy_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f54c2146f0640c54f92e6142ed177bfb5fb8fdd13619bde74c4dfa812741c85b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMinimumHealthyPercent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "desiredCount"))

    @desired_count.setter
    def desired_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__910f5a1202dadf5d0c15c5f36da0b379fb1bca3797de3eb73e88844c22249f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableEcsManagedTags")
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableEcsManagedTags"))

    @enable_ecs_managed_tags.setter
    def enable_ecs_managed_tags(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313ca990559bcccf24f893ee690453cc43ad106b3b7e48d59c3c8b4c700db841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableEcsManagedTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableExecuteCommand")
    def enable_execute_command(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableExecuteCommand"))

    @enable_execute_command.setter
    def enable_execute_command(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78625708600bcbfb0c363a05f29bb8c0bedd6bc6561949b317404323ca4cd943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableExecuteCommand", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66718fe220b73f4154b8444a3b98b93d199d32293b5e7aa902d6b532fcb31b2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="forceNewDeployment")
    def force_new_deployment(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forceNewDeployment"))

    @force_new_deployment.setter
    def force_new_deployment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2b078d0f08e2266596151772d62fb9bcb17eb921a928df6d842d7d5859f3df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceNewDeployment", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckGracePeriodSeconds")
    def health_check_grace_period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthCheckGracePeriodSeconds"))

    @health_check_grace_period_seconds.setter
    def health_check_grace_period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ee43554adc07ff10ac9b55211a79ad652242f8e7eac995b4602d662181b3a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckGracePeriodSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRole")
    def iam_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRole"))

    @iam_role.setter
    def iam_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0e00c0dc5d9997cfc13fe72497408334629b8d066395ae68149fe8c7f5b557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e05f53d472fcb637248e39fd0ab1f6d076ea4127ff138e440378fedc56e2dfac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="launchType")
    def launch_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "launchType"))

    @launch_type.setter
    def launch_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e38435cf7350eed6c7e6e5476d1f87db4b9fedfac66514789c033e9d0d4cf02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302e5f86c9052279ddb7c78bb30b9fd0c32cc72bad621dd82cc36ea01ca97512)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="platformVersion")
    def platform_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformVersion"))

    @platform_version.setter
    def platform_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd51c44bf2d1fb3c8366748b8e6967e7486f4989ba60a4805a5424a1a6d091e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc05eb18dc6623b3cebb8f2685ebde9464fae64afedf3bacdb61e934fa6c34f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategy")
    def scheduling_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulingStrategy"))

    @scheduling_strategy.setter
    def scheduling_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a9ec79be7e01d024ccf014d31c9ff208fa333437448146e697f034db49192b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f55211370165051b256052bfa2b1b9ffdaafdbeb293a910b775af54baa79c44a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aaa903c9afca983406363695cfeeab75eb558a2722a77f7c74e006fc3c27a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="taskDefinition")
    def task_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taskDefinition"))

    @task_definition.setter
    def task_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0df3d383ead5ef1bcfa4e98465e241e4137851c21cb0ef0c4638b9a0b89e23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__700df6a613fd246ccd59966356c822a147217b170ad3ff7d0a916584c89b0597)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="waitForSteadyState")
    def wait_for_steady_state(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForSteadyState"))

    @wait_for_steady_state.setter
    def wait_for_steady_state(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04de3a1313b5583f7e983d2947584c05b3f667965d67401eaa578cb34f1094b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSteadyState", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceAlarms",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_names": "alarmNames",
        "enable": "enable",
        "rollback": "rollback",
    },
)
class EcsServiceAlarms:
    def __init__(
        self,
        *,
        alarm_names: typing.Sequence[builtins.str],
        enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param alarm_names: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarm_names EcsService#alarm_names}.
        :param enable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0236b72b4c3632c5de55dec2520561f5520f31719d92c0f0dc1e0bb01cc5c193)
            check_type(argname="argument alarm_names", value=alarm_names, expected_type=type_hints["alarm_names"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument rollback", value=rollback, expected_type=type_hints["rollback"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_names": alarm_names,
            "enable": enable,
            "rollback": rollback,
        }

    @builtins.property
    def alarm_names(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarm_names EcsService#alarm_names}.'''
        result = self._values.get("alarm_names")
        assert result is not None, "Required property 'alarm_names' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def rollback(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.'''
        result = self._values.get("rollback")
        assert result is not None, "Required property 'rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceAlarms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceAlarmsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceAlarmsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb647e1ae084c86b146c9255210611a51bd5686ead9ec2f0aa44810a6a8cc8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="alarmNamesInput")
    def alarm_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackInput")
    def rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rollbackInput"))

    @builtins.property
    @jsii.member(jsii_name="alarmNames")
    def alarm_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarmNames"))

    @alarm_names.setter
    def alarm_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46b097a464b6698b8d453b0c14882c820b737ab600ddf134c022f94e8fcfd31e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4de458c0af050856fc66146999086628f2292588e42ee8bc47c648fc9702917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rollback")
    def rollback(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rollback"))

    @rollback.setter
    def rollback(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4b1793961eac5e9ce3496f2681259b8c982838a9408c58d990e56dd4aef1490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollback", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceAlarms]:
        return typing.cast(typing.Optional[EcsServiceAlarms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EcsServiceAlarms]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652c3f22a2ace725ac8ac077c128adee3e25cfe361370ca8f995bcc0b1b7fdc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceCapacityProviderStrategy",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider": "capacityProvider",
        "base": "base",
        "weight": "weight",
    },
)
class EcsServiceCapacityProviderStrategy:
    def __init__(
        self,
        *,
        capacity_provider: builtins.str,
        base: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param capacity_provider: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#capacity_provider EcsService#capacity_provider}.
        :param base: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#base EcsService#base}.
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#weight EcsService#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e17a106ff1da4d1f5d9ae25ba4ea4b0a8da3f320ed8d054c999e5d6108dfc83e)
            check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_provider": capacity_provider,
        }
        if base is not None:
            self._values["base"] = base
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def capacity_provider(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#capacity_provider EcsService#capacity_provider}.'''
        result = self._values.get("capacity_provider")
        assert result is not None, "Required property 'capacity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#base EcsService#base}.'''
        result = self._values.get("base")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#weight EcsService#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceCapacityProviderStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceCapacityProviderStrategyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceCapacityProviderStrategyList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690499275c4fde2c17194624fad9a4119decd1b3e5b8bccde02515b10d005378)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceCapacityProviderStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3216f9b65c08d77c9cd0cd5c6d2bba838bfdf6b032cf29affded023c885d031c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceCapacityProviderStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad1bdc38d32f15301e03afe1f969da8bc57d94919116f405b5248af9cd41ae56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a91f5ead406b5180f8e5109a5bb3c8d24745f38ead09896308a5193cdd90565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05fba52eb23c1e5b8b2a5ea47ce2983fccbe54285fb5ef906668ccf895270889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072f99cf4f6a9f7d9c913bfe4bc414f14a2c09915956abe178bbd4fc030b79d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceCapacityProviderStrategyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceCapacityProviderStrategyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d49960a5c1adb0ea66b1ea16234abdb21c2ad4b6ca9d5ebb9d0967dbc870f3c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBase")
    def reset_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBase", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="baseInput")
    def base_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityProviderInput")
    def capacity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="base")
    def base(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "base"))

    @base.setter
    def base(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa5a5783519b5c93e666213ff7d28115b62e97647f12311a114bfb9f7077c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "base", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="capacityProvider")
    def capacity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityProvider"))

    @capacity_provider.setter
    def capacity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0da3f59eb5e8ec9b11241fa93ae7829fa93b2eff6221c686c70cf13fda805fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49cca3312b5355bf429fddba1d45f18b6d53181f689e1702aa0cfa31edfc1002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceCapacityProviderStrategy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceCapacityProviderStrategy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceCapacityProviderStrategy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c9878fbdd64103f4c6e2ccd46ab6341367f6ba76731f892ad100fc11b8463d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "alarms": "alarms",
        "availability_zone_rebalancing": "availabilityZoneRebalancing",
        "capacity_provider_strategy": "capacityProviderStrategy",
        "cluster": "cluster",
        "deployment_circuit_breaker": "deploymentCircuitBreaker",
        "deployment_controller": "deploymentController",
        "deployment_maximum_percent": "deploymentMaximumPercent",
        "deployment_minimum_healthy_percent": "deploymentMinimumHealthyPercent",
        "desired_count": "desiredCount",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "force_delete": "forceDelete",
        "force_new_deployment": "forceNewDeployment",
        "health_check_grace_period_seconds": "healthCheckGracePeriodSeconds",
        "iam_role": "iamRole",
        "id": "id",
        "launch_type": "launchType",
        "load_balancer": "loadBalancer",
        "network_configuration": "networkConfiguration",
        "ordered_placement_strategy": "orderedPlacementStrategy",
        "placement_constraints": "placementConstraints",
        "platform_version": "platformVersion",
        "propagate_tags": "propagateTags",
        "scheduling_strategy": "schedulingStrategy",
        "service_connect_configuration": "serviceConnectConfiguration",
        "service_registries": "serviceRegistries",
        "tags": "tags",
        "tags_all": "tagsAll",
        "task_definition": "taskDefinition",
        "timeouts": "timeouts",
        "triggers": "triggers",
        "volume_configuration": "volumeConfiguration",
        "vpc_lattice_configurations": "vpcLatticeConfigurations",
        "wait_for_steady_state": "waitForSteadyState",
    },
)
class EcsServiceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        alarms: typing.Optional[typing.Union[EcsServiceAlarms, typing.Dict[builtins.str, typing.Any]]] = None,
        availability_zone_rebalancing: typing.Optional[builtins.str] = None,
        capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster: typing.Optional[builtins.str] = None,
        deployment_circuit_breaker: typing.Optional[typing.Union["EcsServiceDeploymentCircuitBreaker", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_controller: typing.Optional[typing.Union["EcsServiceDeploymentController", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_maximum_percent: typing.Optional[jsii.Number] = None,
        deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
        desired_count: typing.Optional[jsii.Number] = None,
        enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        force_new_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
        iam_role: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        launch_type: typing.Optional[builtins.str] = None,
        load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceLoadBalancer", typing.Dict[builtins.str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["EcsServiceNetworkConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        ordered_placement_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceOrderedPlacementStrategy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServicePlacementConstraints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        platform_version: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.str] = None,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        service_connect_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        service_registries: typing.Optional[typing.Union["EcsServiceServiceRegistries", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        task_definition: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["EcsServiceTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume_configuration: typing.Optional[typing.Union["EcsServiceVolumeConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_lattice_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceVpcLatticeConfigurations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.
        :param alarms: alarms block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarms EcsService#alarms}
        :param availability_zone_rebalancing: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#availability_zone_rebalancing EcsService#availability_zone_rebalancing}.
        :param capacity_provider_strategy: capacity_provider_strategy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        :param cluster: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#cluster EcsService#cluster}.
        :param deployment_circuit_breaker: deployment_circuit_breaker block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        :param deployment_controller: deployment_controller block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_controller EcsService#deployment_controller}
        :param deployment_maximum_percent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.
        :param deployment_minimum_healthy_percent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.
        :param desired_count: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#desired_count EcsService#desired_count}.
        :param enable_ecs_managed_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.
        :param enable_execute_command: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_execute_command EcsService#enable_execute_command}.
        :param force_delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_delete EcsService#force_delete}.
        :param force_new_deployment: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_new_deployment EcsService#force_new_deployment}.
        :param health_check_grace_period_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.
        :param iam_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iam_role EcsService#iam_role}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#id EcsService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param launch_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#launch_type EcsService#launch_type}.
        :param load_balancer: load_balancer block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#load_balancer EcsService#load_balancer}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#network_configuration EcsService#network_configuration}
        :param ordered_placement_strategy: ordered_placement_strategy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        :param placement_constraints: placement_constraints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#placement_constraints EcsService#placement_constraints}
        :param platform_version: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#platform_version EcsService#platform_version}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param scheduling_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.
        :param service_connect_configuration: service_connect_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        :param service_registries: service_registries block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_registries EcsService#service_registries}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags EcsService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags_all EcsService#tags_all}.
        :param task_definition: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#task_definition EcsService#task_definition}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#timeouts EcsService#timeouts}
        :param triggers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#triggers EcsService#triggers}.
        :param volume_configuration: volume_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_configuration EcsService#volume_configuration}
        :param vpc_lattice_configurations: vpc_lattice_configurations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#vpc_lattice_configurations EcsService#vpc_lattice_configurations}
        :param wait_for_steady_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alarms, dict):
            alarms = EcsServiceAlarms(**alarms)
        if isinstance(deployment_circuit_breaker, dict):
            deployment_circuit_breaker = EcsServiceDeploymentCircuitBreaker(**deployment_circuit_breaker)
        if isinstance(deployment_controller, dict):
            deployment_controller = EcsServiceDeploymentController(**deployment_controller)
        if isinstance(network_configuration, dict):
            network_configuration = EcsServiceNetworkConfiguration(**network_configuration)
        if isinstance(service_connect_configuration, dict):
            service_connect_configuration = EcsServiceServiceConnectConfiguration(**service_connect_configuration)
        if isinstance(service_registries, dict):
            service_registries = EcsServiceServiceRegistries(**service_registries)
        if isinstance(timeouts, dict):
            timeouts = EcsServiceTimeouts(**timeouts)
        if isinstance(volume_configuration, dict):
            volume_configuration = EcsServiceVolumeConfiguration(**volume_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd06227334c2f29835ac4df8c10ce828d0382b9a4135d3f943ec5d04d412568)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument availability_zone_rebalancing", value=availability_zone_rebalancing, expected_type=type_hints["availability_zone_rebalancing"])
            check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument deployment_circuit_breaker", value=deployment_circuit_breaker, expected_type=type_hints["deployment_circuit_breaker"])
            check_type(argname="argument deployment_controller", value=deployment_controller, expected_type=type_hints["deployment_controller"])
            check_type(argname="argument deployment_maximum_percent", value=deployment_maximum_percent, expected_type=type_hints["deployment_maximum_percent"])
            check_type(argname="argument deployment_minimum_healthy_percent", value=deployment_minimum_healthy_percent, expected_type=type_hints["deployment_minimum_healthy_percent"])
            check_type(argname="argument desired_count", value=desired_count, expected_type=type_hints["desired_count"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument force_new_deployment", value=force_new_deployment, expected_type=type_hints["force_new_deployment"])
            check_type(argname="argument health_check_grace_period_seconds", value=health_check_grace_period_seconds, expected_type=type_hints["health_check_grace_period_seconds"])
            check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument ordered_placement_strategy", value=ordered_placement_strategy, expected_type=type_hints["ordered_placement_strategy"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument scheduling_strategy", value=scheduling_strategy, expected_type=type_hints["scheduling_strategy"])
            check_type(argname="argument service_connect_configuration", value=service_connect_configuration, expected_type=type_hints["service_connect_configuration"])
            check_type(argname="argument service_registries", value=service_registries, expected_type=type_hints["service_registries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
            check_type(argname="argument volume_configuration", value=volume_configuration, expected_type=type_hints["volume_configuration"])
            check_type(argname="argument vpc_lattice_configurations", value=vpc_lattice_configurations, expected_type=type_hints["vpc_lattice_configurations"])
            check_type(argname="argument wait_for_steady_state", value=wait_for_steady_state, expected_type=type_hints["wait_for_steady_state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if alarms is not None:
            self._values["alarms"] = alarms
        if availability_zone_rebalancing is not None:
            self._values["availability_zone_rebalancing"] = availability_zone_rebalancing
        if capacity_provider_strategy is not None:
            self._values["capacity_provider_strategy"] = capacity_provider_strategy
        if cluster is not None:
            self._values["cluster"] = cluster
        if deployment_circuit_breaker is not None:
            self._values["deployment_circuit_breaker"] = deployment_circuit_breaker
        if deployment_controller is not None:
            self._values["deployment_controller"] = deployment_controller
        if deployment_maximum_percent is not None:
            self._values["deployment_maximum_percent"] = deployment_maximum_percent
        if deployment_minimum_healthy_percent is not None:
            self._values["deployment_minimum_healthy_percent"] = deployment_minimum_healthy_percent
        if desired_count is not None:
            self._values["desired_count"] = desired_count
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if force_new_deployment is not None:
            self._values["force_new_deployment"] = force_new_deployment
        if health_check_grace_period_seconds is not None:
            self._values["health_check_grace_period_seconds"] = health_check_grace_period_seconds
        if iam_role is not None:
            self._values["iam_role"] = iam_role
        if id is not None:
            self._values["id"] = id
        if launch_type is not None:
            self._values["launch_type"] = launch_type
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if ordered_placement_strategy is not None:
            self._values["ordered_placement_strategy"] = ordered_placement_strategy
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if scheduling_strategy is not None:
            self._values["scheduling_strategy"] = scheduling_strategy
        if service_connect_configuration is not None:
            self._values["service_connect_configuration"] = service_connect_configuration
        if service_registries is not None:
            self._values["service_registries"] = service_registries
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if task_definition is not None:
            self._values["task_definition"] = task_definition
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if triggers is not None:
            self._values["triggers"] = triggers
        if volume_configuration is not None:
            self._values["volume_configuration"] = volume_configuration
        if vpc_lattice_configurations is not None:
            self._values["vpc_lattice_configurations"] = vpc_lattice_configurations
        if wait_for_steady_state is not None:
            self._values["wait_for_steady_state"] = wait_for_steady_state

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarms(self) -> typing.Optional[EcsServiceAlarms]:
        '''alarms block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#alarms EcsService#alarms}
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[EcsServiceAlarms], result)

    @builtins.property
    def availability_zone_rebalancing(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#availability_zone_rebalancing EcsService#availability_zone_rebalancing}.'''
        result = self._values.get("availability_zone_rebalancing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capacity_provider_strategy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]]:
        '''capacity_provider_strategy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#capacity_provider_strategy EcsService#capacity_provider_strategy}
        '''
        result = self._values.get("capacity_provider_strategy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]], result)

    @builtins.property
    def cluster(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#cluster EcsService#cluster}.'''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_circuit_breaker(
        self,
    ) -> typing.Optional["EcsServiceDeploymentCircuitBreaker"]:
        '''deployment_circuit_breaker block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_circuit_breaker EcsService#deployment_circuit_breaker}
        '''
        result = self._values.get("deployment_circuit_breaker")
        return typing.cast(typing.Optional["EcsServiceDeploymentCircuitBreaker"], result)

    @builtins.property
    def deployment_controller(
        self,
    ) -> typing.Optional["EcsServiceDeploymentController"]:
        '''deployment_controller block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_controller EcsService#deployment_controller}
        '''
        result = self._values.get("deployment_controller")
        return typing.cast(typing.Optional["EcsServiceDeploymentController"], result)

    @builtins.property
    def deployment_maximum_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_maximum_percent EcsService#deployment_maximum_percent}.'''
        result = self._values.get("deployment_maximum_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def deployment_minimum_healthy_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#deployment_minimum_healthy_percent EcsService#deployment_minimum_healthy_percent}.'''
        result = self._values.get("deployment_minimum_healthy_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def desired_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#desired_count EcsService#desired_count}.'''
        result = self._values.get("desired_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enable_ecs_managed_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_ecs_managed_tags EcsService#enable_ecs_managed_tags}.'''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_execute_command(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable_execute_command EcsService#enable_execute_command}.'''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_delete EcsService#force_delete}.'''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def force_new_deployment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#force_new_deployment EcsService#force_new_deployment}.'''
        result = self._values.get("force_new_deployment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def health_check_grace_period_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#health_check_grace_period_seconds EcsService#health_check_grace_period_seconds}.'''
        result = self._values.get("health_check_grace_period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iam_role EcsService#iam_role}.'''
        result = self._values.get("iam_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#id EcsService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#launch_type EcsService#launch_type}.'''
        result = self._values.get("launch_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceLoadBalancer"]]]:
        '''load_balancer block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#load_balancer EcsService#load_balancer}
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceLoadBalancer"]]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional["EcsServiceNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#network_configuration EcsService#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["EcsServiceNetworkConfiguration"], result)

    @builtins.property
    def ordered_placement_strategy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]]:
        '''ordered_placement_strategy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#ordered_placement_strategy EcsService#ordered_placement_strategy}
        '''
        result = self._values.get("ordered_placement_strategy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceOrderedPlacementStrategy"]]], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServicePlacementConstraints"]]]:
        '''placement_constraints block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#placement_constraints EcsService#placement_constraints}
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServicePlacementConstraints"]]], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#platform_version EcsService#platform_version}.'''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#propagate_tags EcsService#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#scheduling_strategy EcsService#scheduling_strategy}.'''
        result = self._values.get("scheduling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_connect_configuration(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfiguration"]:
        '''service_connect_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_connect_configuration EcsService#service_connect_configuration}
        '''
        result = self._values.get("service_connect_configuration")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfiguration"], result)

    @builtins.property
    def service_registries(self) -> typing.Optional["EcsServiceServiceRegistries"]:
        '''service_registries block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service_registries EcsService#service_registries}
        '''
        result = self._values.get("service_registries")
        return typing.cast(typing.Optional["EcsServiceServiceRegistries"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags EcsService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags_all EcsService#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def task_definition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#task_definition EcsService#task_definition}.'''
        result = self._values.get("task_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["EcsServiceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#timeouts EcsService#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["EcsServiceTimeouts"], result)

    @builtins.property
    def triggers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#triggers EcsService#triggers}.'''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def volume_configuration(self) -> typing.Optional["EcsServiceVolumeConfiguration"]:
        '''volume_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_configuration EcsService#volume_configuration}
        '''
        result = self._values.get("volume_configuration")
        return typing.cast(typing.Optional["EcsServiceVolumeConfiguration"], result)

    @builtins.property
    def vpc_lattice_configurations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVpcLatticeConfigurations"]]]:
        '''vpc_lattice_configurations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#vpc_lattice_configurations EcsService#vpc_lattice_configurations}
        '''
        result = self._values.get("vpc_lattice_configurations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVpcLatticeConfigurations"]]], result)

    @builtins.property
    def wait_for_steady_state(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#wait_for_steady_state EcsService#wait_for_steady_state}.'''
        result = self._values.get("wait_for_steady_state")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceDeploymentCircuitBreaker",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable", "rollback": "rollback"},
)
class EcsServiceDeploymentCircuitBreaker:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enable: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.
        :param rollback: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd544fef19ed11253d9f4d8f7cc38ce853204dd3d738f660413d9c0fb3dfcce)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument rollback", value=rollback, expected_type=type_hints["rollback"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enable": enable,
            "rollback": rollback,
        }

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enable EcsService#enable}.'''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def rollback(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#rollback EcsService#rollback}.'''
        result = self._values.get("rollback")
        assert result is not None, "Required property 'rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentCircuitBreaker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentCircuitBreakerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceDeploymentCircuitBreakerOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96fb61a0e890a8c246b7b37f43ae2158e533ff96dd1d55ebbbc8f9ad6635b387)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackInput")
    def rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rollbackInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__525eada7d1b28b6625022f9e967e80f9b9ff92a493632c0c8ba805070cc4949a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rollback")
    def rollback(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rollback"))

    @rollback.setter
    def rollback(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__443e6f1767f767022d0bc5727875f4b274f671a86d0e9176619e6ce68513a34c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollback", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentCircuitBreaker]:
        return typing.cast(typing.Optional[EcsServiceDeploymentCircuitBreaker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentCircuitBreaker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__426c0d62a39fe666930412c7ac47957a69329df70bbeb25b3c6097c4b4aef303)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceDeploymentController",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class EcsServiceDeploymentController:
    def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c734efd8ce7f47bf93f561d582cb059d1826da611c2844fc62ff8415073e278)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceDeploymentController(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceDeploymentControllerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceDeploymentControllerOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b384797f044bfc97b63fc8e7e752475c3181b1dade08d76b75467db2b6f6851f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e20f5bfff0c215b8e41f581972b615856787c18dd4765f80ddfed8bbd4e7bd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceDeploymentController]:
        return typing.cast(typing.Optional[EcsServiceDeploymentController], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceDeploymentController],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b7851c942aec497e92e5c2469e10e6d4a87349879297c8771b4e92135bd7de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceLoadBalancer",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "container_port": "containerPort",
        "elb_name": "elbName",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsServiceLoadBalancer:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        container_port: jsii.Number,
        elb_name: typing.Optional[builtins.str] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_port EcsService#container_port}.
        :param elb_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#elb_name EcsService#elb_name}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#target_group_arn EcsService#target_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43301010cd18d6073ed4b6f5f536641ad5625729ee1d9f32d5ea87d03e27254)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument elb_name", value=elb_name, expected_type=type_hints["elb_name"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_name": container_name,
            "container_port": container_port,
        }
        if elb_name is not None:
            self._values["elb_name"] = elb_name
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        assert result is not None, "Required property 'container_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def elb_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#elb_name EcsService#elb_name}.'''
        result = self._values.get("elb_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#target_group_arn EcsService#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceLoadBalancer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceLoadBalancerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceLoadBalancerList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53c2eeceeee0fe93db6e9bfd209ff4bd5cb20388ccd44e3e61f7da9d5f51a19)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EcsServiceLoadBalancerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41ead0c9e9e9de74ad556b1a3c02eb7bc64e222f0c896989b5b111f4a7a91df3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceLoadBalancerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154fdd5c7b2ac7da2fb93c260e7e037b313ff71baa7353e2e4e7dfd571b112f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dcaefa87b4d925355bbf9cded6b7249c77fa6e5d7153a992e8f00b2faeb0066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__364853fc608744c8683c4fd01b774bd28d57b42625f3fce6367c8c9035a5e963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceLoadBalancer]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceLoadBalancer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceLoadBalancer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3b21d60b0b42f25493b9ac64e8e02dff80a3da53cd71ad46a9d050747b2319)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceLoadBalancerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceLoadBalancerOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17492237fd499c46c35dd4ffb1d0d2ed0826481c6fb762408777920b22269816)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetElbName")
    def reset_elb_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElbName", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="elbNameInput")
    def elb_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59590190fd6e4c85afeb6ccefa1680e67cd20d159ed936e47a1751c9f6af6c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31261925bf84f447136d44a1c724bdf810b35124e3901f541a1bd84ee8699e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elbName")
    def elb_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elbName"))

    @elb_name.setter
    def elb_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccef3159d41aee6d6e50dcc6abf5ae9b53f97303a88bc4503f25fce0f0296cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elbName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe424d03bdbadb2b1f37dfb265be0985d9e3dd905aeef7368c9b46173a7930f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceLoadBalancer]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceLoadBalancer]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceLoadBalancer]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790b1e1ab99900de908b6f7691afa448396ef46e98c2eede9b3dd1bf25819186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "assign_public_ip": "assignPublicIp",
        "security_groups": "securityGroups",
    },
)
class EcsServiceNetworkConfiguration:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnets: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#subnets EcsService#subnets}.
        :param assign_public_ip: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#assign_public_ip EcsService#assign_public_ip}.
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#security_groups EcsService#security_groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e6cc44d9afd037522d6dd54e09e5f1f58098dbacc3ff1b665bcf53bc443d74)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnets": subnets,
        }
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if security_groups is not None:
            self._values["security_groups"] = security_groups

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#subnets EcsService#subnets}.'''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assign_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#assign_public_ip EcsService#assign_public_ip}.'''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#security_groups EcsService#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceNetworkConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceNetworkConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4165cc3e809d5f2017474531df70935454aafba146dcc1b1f65402b854ab84cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssignPublicIp")
    def reset_assign_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssignPublicIp", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIpInput")
    def assign_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "assignPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetsInput")
    def subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "assignPublicIp"))

    @assign_public_ip.setter
    def assign_public_ip(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06521eed398e5449af9731c85f59146082134ee4e921d06edcd835a99724da19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assignPublicIp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b01d8f6d390d8b7e9f5169f74bf59770f9154f337069839cc98bd6da43b3326d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c5d035ae2ec4256e9259ca5df2b41875484e6fecdee0250e3f05c0201c2e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceNetworkConfiguration]:
        return typing.cast(typing.Optional[EcsServiceNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e69498fe504da84ec958188e5e1e6aafc4246b8105076aeb521bf73f1da693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceOrderedPlacementStrategy",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "field": "field"},
)
class EcsServiceOrderedPlacementStrategy:
    def __init__(
        self,
        *,
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.
        :param field: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#field EcsService#field}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b2fa02c5ee0700f3450427062fbfa1178032fce4ed5897958d2112e5df0e2d0)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#field EcsService#field}.'''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceOrderedPlacementStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceOrderedPlacementStrategyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceOrderedPlacementStrategyList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6fb2f946b7987282e5b0b857c03ba822a5c1e659705a01f23d436dc0f2eaf8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceOrderedPlacementStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e0c042bc787756d8163d70ba79ab5c9191bb251a8a0baa978b48d5f0395188)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceOrderedPlacementStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8388444d4b284fc348c59328cd0f8fe4e78df0c4e8ee9ea63af82c778a86c0d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b637f7cf479016698612bf153359a5663b91110267b39da1b3b7f61c60981845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ca22af699247f311c781f495c69532c31ab0ad8f234e6f3ef73d71b7430151)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf5e4205d6fd99c86e8cce51da0dfd03f89d615d293006587290f5cb96a213c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceOrderedPlacementStrategyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceOrderedPlacementStrategyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b36da589f0e632ecae9266be8f8b1b2233952f052f07e3c3250a136dbdd7a0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f847ebc948cbab0441e4037ee8aec3c1590f7d3b82dd920a03a078bf9cc24c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1363e51f54f40bf5732d0299c347c3139e709e45eb935ed797579f7011de95f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceOrderedPlacementStrategy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceOrderedPlacementStrategy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceOrderedPlacementStrategy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4dd7d1a769de9b0dfb5f5a378fe4f958ae89fd1242de2f85439a604b7ed223e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServicePlacementConstraints",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expression": "expression"},
)
class EcsServicePlacementConstraints:
    def __init__(
        self,
        *,
        type: builtins.str,
        expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.
        :param expression: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#expression EcsService#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca6dead5764b3362f489002ae19f9df8369566a8e660c320d82fe37eb7fa5a0)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#type EcsService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#expression EcsService#expression}.'''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServicePlacementConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServicePlacementConstraintsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServicePlacementConstraintsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccc635750032622d26096a7358537cca9b8699aa3d5088221586e14f4c8f9b64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServicePlacementConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__899b506235dce009d82ad235e82b6b907703a8390f77397ffdd7f750bb36a2f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServicePlacementConstraintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e9aeea76170bb7f6eb39faaca77c47c2f8524c0973e2f091eec8d3b2397241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f1836da08448d685e37fc37d7ec63a8d33bffa7c7905badd5f5b806bfd3e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d33fcead1c9627f5ec752c30132fbb3d4ea07904ec87d14b4c6f9ca322019af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServicePlacementConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServicePlacementConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServicePlacementConstraints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e554fdfac315791a20270262edeb994b329a22082eb5d7b777454b8fe7e83f08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServicePlacementConstraintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServicePlacementConstraintsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94f69f23c62b4276d4f78ab0b218cf7d4f24c946a24c9bbe70a4fa035d97f929)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00b130d3a60a3a3467defb1c63e4066a2d009782650fbc521f26c805942d84df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4daaa45b89e7f33994d222113202dfd0c6857704404f7d3ea67296052888f7ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServicePlacementConstraints]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServicePlacementConstraints]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServicePlacementConstraints]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33f45c4f20c8586666e1ac40630fd774dc4a0b3ace5505711e86ab66fa6f4705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "log_configuration": "logConfiguration",
        "namespace": "namespace",
        "service": "service",
    },
)
class EcsServiceServiceConnectConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        log_configuration: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationLogConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        namespace: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationService", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enabled EcsService#enabled}.
        :param log_configuration: log_configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_configuration EcsService#log_configuration}
        :param namespace: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#namespace EcsService#namespace}.
        :param service: service block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service EcsService#service}
        '''
        if isinstance(log_configuration, dict):
            log_configuration = EcsServiceServiceConnectConfigurationLogConfiguration(**log_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a36c700ffce96721bb674a30a401e035df2f3da4a64a8440ea1610bfc704b3a)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument log_configuration", value=log_configuration, expected_type=type_hints["log_configuration"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if log_configuration is not None:
            self._values["log_configuration"] = log_configuration
        if namespace is not None:
            self._values["namespace"] = namespace
        if service is not None:
            self._values["service"] = service

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#enabled EcsService#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def log_configuration(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationLogConfiguration"]:
        '''log_configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_configuration EcsService#log_configuration}
        '''
        result = self._values.get("log_configuration")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationLogConfiguration"], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#namespace EcsService#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationService"]]]:
        '''service block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#service EcsService#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationService"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationLogConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "log_driver": "logDriver",
        "options": "options",
        "secret_option": "secretOption",
    },
)
class EcsServiceServiceConnectConfigurationLogConfiguration:
    def __init__(
        self,
        *,
        log_driver: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secret_option: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param log_driver: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_driver EcsService#log_driver}.
        :param options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#options EcsService#options}.
        :param secret_option: secret_option block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#secret_option EcsService#secret_option}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b994ea1dfb29104d881f1785df924404392b77f02d6747bd98f9f59ea4000c6f)
            check_type(argname="argument log_driver", value=log_driver, expected_type=type_hints["log_driver"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument secret_option", value=secret_option, expected_type=type_hints["secret_option"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_driver": log_driver,
        }
        if options is not None:
            self._values["options"] = options
        if secret_option is not None:
            self._values["secret_option"] = secret_option

    @builtins.property
    def log_driver(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_driver EcsService#log_driver}.'''
        result = self._values.get("log_driver")
        assert result is not None, "Required property 'log_driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#options EcsService#options}.'''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def secret_option(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]]:
        '''secret_option block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#secret_option EcsService#secret_option}
        '''
        result = self._values.get("secret_option")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationLogConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationLogConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a3f5b4700e5df9dd52665c77bec31b0aaba4ee9d67fd6a6d5487e80e0e8125)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretOption")
    def put_secret_option(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739a5eb9090eb5a505d7344b4e04c376ef0d8ac69b54836717c5918ff5910a92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecretOption", [value]))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetSecretOption")
    def reset_secret_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretOption", []))

    @builtins.property
    @jsii.member(jsii_name="secretOption")
    def secret_option(
        self,
    ) -> "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList":
        return typing.cast("EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList", jsii.get(self, "secretOption"))

    @builtins.property
    @jsii.member(jsii_name="logDriverInput")
    def log_driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDriverInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="secretOptionInput")
    def secret_option_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationLogConfigurationSecretOption"]]], jsii.get(self, "secretOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDriver"))

    @log_driver.setter
    def log_driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a85d40e624ec67f7a7e6e9332f2b62d43c3e6bcdd5f75473ad13dd77beffbfcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDriver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dabaa670e16c08e2b56d7c81ca20b479f0b6a6f70af5232fa5522f803eca6b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff1a15e5b7032e945228317440d554206140bbcdef9441a4d9b27ce974ae5f80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOption",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value_from": "valueFrom"},
)
class EcsServiceServiceConnectConfigurationLogConfigurationSecretOption:
    def __init__(self, *, name: builtins.str, value_from: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.
        :param value_from: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#value_from EcsService#value_from}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d601e6b26d92ec645e67f0df4877eee7511694d3555f9812e6e7b581a4b150f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value_from", value=value_from, expected_type=type_hints["value_from"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value_from": value_from,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_from(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#value_from EcsService#value_from}.'''
        result = self._values.get("value_from")
        assert result is not None, "Required property 'value_from' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationLogConfigurationSecretOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38bf5c3c786c2e131802a8d15ed391f74fd5453b7e5303fcf73aaaf8ff99f738)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fea7bf5eb8e8ad1b39ecd5afac52b0272242c523ae743e90eb6463dbb506c34)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391596afcb6da7cc10b1091820ba3e9f2b315c3a2365f9e6f298d183a12e79af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffefa7580b4d5f396a09195cffb8834e9b6ae30d598fee794af1fc10347ee54a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__097caf2df780bedc54752fcc54bcf18a1f87cfe57827137cec3f1bd5f6a6c1b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35dac268da65f166b0003d9ca1e6c9b697b072522d52119cff112607c06d05f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f0b2ed23fac04d1144233eeaedda55483d6ac0857470e8bac00e6c81f2c670)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFromInput")
    def value_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueFromInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a86556f7df913e54df08a6e4ccf21a7072b2715cadb5000bff1d0fde81cea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="valueFrom")
    def value_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueFrom"))

    @value_from.setter
    def value_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb7970a829314cf79027952be4a6d5127b594607b5e264d7a33c4232c227c840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueFrom", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0541c8e2191396bb7378436b9cadfcb649bf8c4badc4ca90750dc7dc8614402c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceServiceConnectConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d005cfcdb7408ad8d4650db266c9b91260f5cfd6d744caa6168c9616bac9f523)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLogConfiguration")
    def put_log_configuration(
        self,
        *,
        log_driver: builtins.str,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        secret_option: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param log_driver: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#log_driver EcsService#log_driver}.
        :param options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#options EcsService#options}.
        :param secret_option: secret_option block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#secret_option EcsService#secret_option}
        '''
        value = EcsServiceServiceConnectConfigurationLogConfiguration(
            log_driver=log_driver, options=options, secret_option=secret_option
        )

        return typing.cast(None, jsii.invoke(self, "putLogConfiguration", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceServiceConnectConfigurationService", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92aa69acd12070b1561de0490e8c790c09327b3ecc011cf29eae28025f79ae60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="resetLogConfiguration")
    def reset_log_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfiguration", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @builtins.property
    @jsii.member(jsii_name="logConfiguration")
    def log_configuration(
        self,
    ) -> EcsServiceServiceConnectConfigurationLogConfigurationOutputReference:
        return typing.cast(EcsServiceServiceConnectConfigurationLogConfigurationOutputReference, jsii.get(self, "logConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "EcsServiceServiceConnectConfigurationServiceList":
        return typing.cast("EcsServiceServiceConnectConfigurationServiceList", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigurationInput")
    def log_configuration_input(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration], jsii.get(self, "logConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationService"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceServiceConnectConfigurationService"]]], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__840f9603b0b3c67930ed47e8082be1f5f3a682cbc9995ac5229a6a12ca35b365)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7619f9f8cc023211abb9d0c3a27df69b217e6d7068e2bb9dc682e5653d6a380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceServiceConnectConfiguration]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59bcdc329a7616fb4108ac0c0748e198659147134420a0b469db2745619ee6f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationService",
    jsii_struct_bases=[],
    name_mapping={
        "port_name": "portName",
        "client_alias": "clientAlias",
        "discovery_name": "discoveryName",
        "ingress_port_override": "ingressPortOverride",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class EcsServiceServiceConnectConfigurationService:
    def __init__(
        self,
        *,
        port_name: builtins.str,
        client_alias: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationServiceClientAlias", typing.Dict[builtins.str, typing.Any]]] = None,
        discovery_name: typing.Optional[builtins.str] = None,
        ingress_port_override: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationServiceTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["EcsServiceServiceConnectConfigurationServiceTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port_name EcsService#port_name}.
        :param client_alias: client_alias block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#client_alias EcsService#client_alias}
        :param discovery_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#discovery_name EcsService#discovery_name}.
        :param ingress_port_override: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#ingress_port_override EcsService#ingress_port_override}.
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#timeout EcsService#timeout}
        :param tls: tls block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tls EcsService#tls}
        '''
        if isinstance(client_alias, dict):
            client_alias = EcsServiceServiceConnectConfigurationServiceClientAlias(**client_alias)
        if isinstance(timeout, dict):
            timeout = EcsServiceServiceConnectConfigurationServiceTimeout(**timeout)
        if isinstance(tls, dict):
            tls = EcsServiceServiceConnectConfigurationServiceTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393fa0a93131289bc28987cc899fb914f3b9a3f15c6a5e077275b46c5b30e394)
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument client_alias", value=client_alias, expected_type=type_hints["client_alias"])
            check_type(argname="argument discovery_name", value=discovery_name, expected_type=type_hints["discovery_name"])
            check_type(argname="argument ingress_port_override", value=ingress_port_override, expected_type=type_hints["ingress_port_override"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port_name": port_name,
        }
        if client_alias is not None:
            self._values["client_alias"] = client_alias
        if discovery_name is not None:
            self._values["discovery_name"] = discovery_name
        if ingress_port_override is not None:
            self._values["ingress_port_override"] = ingress_port_override
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def port_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port_name EcsService#port_name}.'''
        result = self._values.get("port_name")
        assert result is not None, "Required property 'port_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_alias(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationServiceClientAlias"]:
        '''client_alias block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#client_alias EcsService#client_alias}
        '''
        result = self._values.get("client_alias")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationServiceClientAlias"], result)

    @builtins.property
    def discovery_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#discovery_name EcsService#discovery_name}.'''
        result = self._values.get("discovery_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_port_override(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#ingress_port_override EcsService#ingress_port_override}.'''
        result = self._values.get("ingress_port_override")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationServiceTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#timeout EcsService#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationServiceTimeout"], result)

    @builtins.property
    def tls(self) -> typing.Optional["EcsServiceServiceConnectConfigurationServiceTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tls EcsService#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationServiceTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceClientAlias",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "dns_name": "dnsName"},
)
class EcsServiceServiceConnectConfigurationServiceClientAlias:
    def __init__(
        self,
        *,
        port: jsii.Number,
        dns_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.
        :param dns_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#dns_name EcsService#dns_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd09bd41bb46ea4f2e707299517224725fadff30ec2321ea22dad3d495f9c5f)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
        }
        if dns_name is not None:
            self._values["dns_name"] = dns_name

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dns_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#dns_name EcsService#dns_name}.'''
        result = self._values.get("dns_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationServiceClientAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53966912423f8d25c38414fa638067ec8798cc99a272bc15ae8920a2d66f1bdf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDnsName")
    def reset_dns_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsName", []))

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300650857892dfa4c099a739254f648e0a962abca0da4b8a57f1d348402fd9b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ce1a8b0f4531ab7b405ec614be289beae16279c7b00bd7172e5d72f86ea1e36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1006bfa48d8e2e637f13214e6f3ee22c1d176fdc1a1c199b79d1c4369b816ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceServiceConnectConfigurationServiceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__051417a6d80dba73e39f14156ec15547f316ae677bcffba32f32e744284132c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceServiceConnectConfigurationServiceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0dfcb25f9262a528231d260c2ff59e964a82757dad71eb6acf9fca2c54897ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceServiceConnectConfigurationServiceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b28b236a23932aeb6f20501bc6ed14000d376bbb3ea4203769f3c6e03a78c503)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e8f8370d26e0bef4d2c4bbf1294c76eab3e693756873876c99b01c60fbf74f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d81a261a8d520412090c15e847777da7ebfd839b1eb98845e2a01163549b1574)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationService]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationService]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationService]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62bec76c00b51e254290fc53d44852de3bd6dbb3ed69dd0dc0e5a01f37122c31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceServiceConnectConfigurationServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c6e8dd21747629f4aa425e2b7457d90a2952da373309934f00a9ffa8a102ef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClientAlias")
    def put_client_alias(
        self,
        *,
        port: jsii.Number,
        dns_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.
        :param dns_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#dns_name EcsService#dns_name}.
        '''
        value = EcsServiceServiceConnectConfigurationServiceClientAlias(
            port=port, dns_name=dns_name
        )

        return typing.cast(None, jsii.invoke(self, "putClientAlias", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        idle_timeout_seconds: typing.Optional[jsii.Number] = None,
        per_request_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#idle_timeout_seconds EcsService#idle_timeout_seconds}.
        :param per_request_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#per_request_timeout_seconds EcsService#per_request_timeout_seconds}.
        '''
        value = EcsServiceServiceConnectConfigurationServiceTimeout(
            idle_timeout_seconds=idle_timeout_seconds,
            per_request_timeout_seconds=per_request_timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        issuer_cert_authority: typing.Union["EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority", typing.Dict[builtins.str, typing.Any]],
        kms_key: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param issuer_cert_authority: issuer_cert_authority block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#issuer_cert_authority EcsService#issuer_cert_authority}
        :param kms_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key EcsService#kms_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.
        '''
        value = EcsServiceServiceConnectConfigurationServiceTls(
            issuer_cert_authority=issuer_cert_authority,
            kms_key=kms_key,
            role_arn=role_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetClientAlias")
    def reset_client_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAlias", []))

    @jsii.member(jsii_name="resetDiscoveryName")
    def reset_discovery_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscoveryName", []))

    @jsii.member(jsii_name="resetIngressPortOverride")
    def reset_ingress_port_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressPortOverride", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="clientAlias")
    def client_alias(
        self,
    ) -> EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference:
        return typing.cast(EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference, jsii.get(self, "clientAlias"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(
        self,
    ) -> "EcsServiceServiceConnectConfigurationServiceTimeoutOutputReference":
        return typing.cast("EcsServiceServiceConnectConfigurationServiceTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "EcsServiceServiceConnectConfigurationServiceTlsOutputReference":
        return typing.cast("EcsServiceServiceConnectConfigurationServiceTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="clientAliasInput")
    def client_alias_input(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias], jsii.get(self, "clientAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="discoveryNameInput")
    def discovery_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "discoveryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressPortOverrideInput")
    def ingress_port_override_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingressPortOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationServiceTimeout"]:
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationServiceTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["EcsServiceServiceConnectConfigurationServiceTls"]:
        return typing.cast(typing.Optional["EcsServiceServiceConnectConfigurationServiceTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="discoveryName")
    def discovery_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "discoveryName"))

    @discovery_name.setter
    def discovery_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22160f5404a257b6ab47eaa563c56d713250a4b7a63e1a4ec0701dd55c073f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "discoveryName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ingressPortOverride")
    def ingress_port_override(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ingressPortOverride"))

    @ingress_port_override.setter
    def ingress_port_override(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e114371bec53e5eebab53b7a5277d7d26cded1fd56f10c6bee2a5437354bf80c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressPortOverride", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec443c3482179e5d719595dfc2bf664f56834dd4274dfa116843ba07e3fc76b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationService]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationService]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationService]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e1233b63434dce3afebdbfd049698487d0539f90a3c7c1b83419f66ce7f1130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTimeout",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_seconds": "idleTimeoutSeconds",
        "per_request_timeout_seconds": "perRequestTimeoutSeconds",
    },
)
class EcsServiceServiceConnectConfigurationServiceTimeout:
    def __init__(
        self,
        *,
        idle_timeout_seconds: typing.Optional[jsii.Number] = None,
        per_request_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#idle_timeout_seconds EcsService#idle_timeout_seconds}.
        :param per_request_timeout_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#per_request_timeout_seconds EcsService#per_request_timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3b919fad4722129f59b1d91f451b54dfaec4e1ad11b12b1ba0389ee2151ce4)
            check_type(argname="argument idle_timeout_seconds", value=idle_timeout_seconds, expected_type=type_hints["idle_timeout_seconds"])
            check_type(argname="argument per_request_timeout_seconds", value=per_request_timeout_seconds, expected_type=type_hints["per_request_timeout_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_timeout_seconds is not None:
            self._values["idle_timeout_seconds"] = idle_timeout_seconds
        if per_request_timeout_seconds is not None:
            self._values["per_request_timeout_seconds"] = per_request_timeout_seconds

    @builtins.property
    def idle_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#idle_timeout_seconds EcsService#idle_timeout_seconds}.'''
        result = self._values.get("idle_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def per_request_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#per_request_timeout_seconds EcsService#per_request_timeout_seconds}.'''
        result = self._values.get("per_request_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationServiceTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationServiceTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTimeoutOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67614d8cd89acc79cd9869dda5b1e246930270c352b4909e0ba7ec995369400)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutSeconds")
    def reset_idle_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutSeconds", []))

    @jsii.member(jsii_name="resetPerRequestTimeoutSeconds")
    def reset_per_request_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequestTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutSecondsInput")
    def idle_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestTimeoutSecondsInput")
    def per_request_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "perRequestTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutSeconds")
    def idle_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutSeconds"))

    @idle_timeout_seconds.setter
    def idle_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b8e36a07cc839b6de4db59dd5b3cb450621a7d6f6e2fba9a0bd655aa9b7832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="perRequestTimeoutSeconds")
    def per_request_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "perRequestTimeoutSeconds"))

    @per_request_timeout_seconds.setter
    def per_request_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca0a991877fb607d539ea50ad38d286fa3a3a7ba60c93303fafaa9b00c0958aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "perRequestTimeoutSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceTimeout]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffcae1dae1e4f494f00f73ac8870a7f1227c1c267ce2f740d816444074952c3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTls",
    jsii_struct_bases=[],
    name_mapping={
        "issuer_cert_authority": "issuerCertAuthority",
        "kms_key": "kmsKey",
        "role_arn": "roleArn",
    },
)
class EcsServiceServiceConnectConfigurationServiceTls:
    def __init__(
        self,
        *,
        issuer_cert_authority: typing.Union["EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority", typing.Dict[builtins.str, typing.Any]],
        kms_key: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param issuer_cert_authority: issuer_cert_authority block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#issuer_cert_authority EcsService#issuer_cert_authority}
        :param kms_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key EcsService#kms_key}.
        :param role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.
        '''
        if isinstance(issuer_cert_authority, dict):
            issuer_cert_authority = EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority(**issuer_cert_authority)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129cbd0cf3a568863742a0434cbf5a99af649a91e66358679f3df08cbe477e7f)
            check_type(argname="argument issuer_cert_authority", value=issuer_cert_authority, expected_type=type_hints["issuer_cert_authority"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "issuer_cert_authority": issuer_cert_authority,
        }
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def issuer_cert_authority(
        self,
    ) -> "EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority":
        '''issuer_cert_authority block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#issuer_cert_authority EcsService#issuer_cert_authority}
        '''
        result = self._values.get("issuer_cert_authority")
        assert result is not None, "Required property 'issuer_cert_authority' is missing"
        return typing.cast("EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority", result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key EcsService#kms_key}.'''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationServiceTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority",
    jsii_struct_bases=[],
    name_mapping={"aws_pca_authority_arn": "awsPcaAuthorityArn"},
)
class EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority:
    def __init__(self, *, aws_pca_authority_arn: builtins.str) -> None:
        '''
        :param aws_pca_authority_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#aws_pca_authority_arn EcsService#aws_pca_authority_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__628b293eece7db44f48da69f72256ea536a0e0c5db7db5469c04d73f3c50d452)
            check_type(argname="argument aws_pca_authority_arn", value=aws_pca_authority_arn, expected_type=type_hints["aws_pca_authority_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_pca_authority_arn": aws_pca_authority_arn,
        }

    @builtins.property
    def aws_pca_authority_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#aws_pca_authority_arn EcsService#aws_pca_authority_arn}.'''
        result = self._values.get("aws_pca_authority_arn")
        assert result is not None, "Required property 'aws_pca_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa902297f7a8eff9c46e0bddee7191b591bd4a32d8a7a1465a99e70428e36ff1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="awsPcaAuthorityArnInput")
    def aws_pca_authority_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsPcaAuthorityArnInput"))

    @builtins.property
    @jsii.member(jsii_name="awsPcaAuthorityArn")
    def aws_pca_authority_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsPcaAuthorityArn"))

    @aws_pca_authority_arn.setter
    def aws_pca_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__761aecb98886ea91e8a89b05580b954f7edad343290e0eb17edd9b3bb612e254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsPcaAuthorityArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802b5cb710914afbd784878dd3a1f06c888fadca6d2dba40d328a2213cd8f583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceServiceConnectConfigurationServiceTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceConnectConfigurationServiceTlsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a947dfde7a9d26d740fd570a082371a5228f526d13e5f100201867c1330d24e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIssuerCertAuthority")
    def put_issuer_cert_authority(self, *, aws_pca_authority_arn: builtins.str) -> None:
        '''
        :param aws_pca_authority_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#aws_pca_authority_arn EcsService#aws_pca_authority_arn}.
        '''
        value = EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority(
            aws_pca_authority_arn=aws_pca_authority_arn
        )

        return typing.cast(None, jsii.invoke(self, "putIssuerCertAuthority", [value]))

    @jsii.member(jsii_name="resetKmsKey")
    def reset_kms_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKey", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="issuerCertAuthority")
    def issuer_cert_authority(
        self,
    ) -> EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityOutputReference:
        return typing.cast(EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityOutputReference, jsii.get(self, "issuerCertAuthority"))

    @builtins.property
    @jsii.member(jsii_name="issuerCertAuthorityInput")
    def issuer_cert_authority_input(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority], jsii.get(self, "issuerCertAuthorityInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4079b4b254cdb3adecd85138c2d1cdac505a72b88b60250b3fc34ede13652c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253074588ab89f3de6140a21237b42b500d78766000bc879af2a8d3ee7632222)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceServiceConnectConfigurationServiceTls]:
        return typing.cast(typing.Optional[EcsServiceServiceConnectConfigurationServiceTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044bded658d1c6f3976747ae4f1aa01123dd07c96909eb1dd739b2dd6560209a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceServiceRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "registry_arn": "registryArn",
        "container_name": "containerName",
        "container_port": "containerPort",
        "port": "port",
    },
)
class EcsServiceServiceRegistries:
    def __init__(
        self,
        *,
        registry_arn: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        container_port: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param registry_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#registry_arn EcsService#registry_arn}.
        :param container_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_name EcsService#container_name}.
        :param container_port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_port EcsService#container_port}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4100c9e3181d870eb2e7c717677a77b5720df463be07499b88a2e88f9a84d747)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument container_port", value=container_port, expected_type=type_hints["container_port"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if container_port is not None:
            self._values["container_port"] = container_port
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#registry_arn EcsService#registry_arn}.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_name EcsService#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#container_port EcsService#container_port}.'''
        result = self._values.get("container_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port EcsService#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceServiceRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceServiceRegistriesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceServiceRegistriesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982993001259ee192b695778f2d921d0f1ebe01b16b90301854fadbc49f9f6dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetContainerPort")
    def reset_container_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerPort", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="containerPortInput")
    def container_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="registryArnInput")
    def registry_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryArnInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f8f13d84b0f0a57cb0e0037c51a16c19d5c989702f2ed9f217b8686a3e1ea3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerPort")
    def container_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerPort"))

    @container_port.setter
    def container_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebb32577796872f39d9c727f67541066c8b450a81f0792b1ae807f7068d42ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a71be5c7524b3fa68e74a9ba9f65c373510ecbafa39cb6ed76dbdb79baf3d2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="registryArn")
    def registry_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryArn"))

    @registry_arn.setter
    def registry_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ee5b6863ff387d7572995061a3a10d42128c66033ba591f26d1513034b6bf5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceServiceRegistries]:
        return typing.cast(typing.Optional[EcsServiceServiceRegistries], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceServiceRegistries],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1fdf4414cd92685ab943ea669922022d881ff458252825962b233941d79dfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class EcsServiceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#create EcsService#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#delete EcsService#delete}.
        :param update: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#update EcsService#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e692230dc0dcb4d24210eac41f91326cb0ff028aa64838e480d23d8549d43fc)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#create EcsService#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#delete EcsService#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#update EcsService#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b837eb063f394c219ec80fa8e46375df1158321e903bcb367cdd5a100da81ba5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056bd135dc818617b99c74060604c439ccddd136f96152404d0a0dbac0dcf16d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81196a834f5ba4bf4b6e25b5b3a1aa94df1a68e0c2fa65c2a6882ef05f00835d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734dba84c459351bcca614fb68fde308747b0c0864ee9ebf58e19d4609e7f673)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed87d28341b67076c9dec1d8cf79a1d3ef92432f857274b6024e5be34916ce9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceVolumeConfiguration",
    jsii_struct_bases=[],
    name_mapping={"managed_ebs_volume": "managedEbsVolume", "name": "name"},
)
class EcsServiceVolumeConfiguration:
    def __init__(
        self,
        *,
        managed_ebs_volume: typing.Union["EcsServiceVolumeConfigurationManagedEbsVolume", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
    ) -> None:
        '''
        :param managed_ebs_volume: managed_ebs_volume block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#managed_ebs_volume EcsService#managed_ebs_volume}
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.
        '''
        if isinstance(managed_ebs_volume, dict):
            managed_ebs_volume = EcsServiceVolumeConfigurationManagedEbsVolume(**managed_ebs_volume)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6911ab88651a2ab29d5dcf6aa67a78707c0e09f6fc9d846ccbf2286f6139cb8)
            check_type(argname="argument managed_ebs_volume", value=managed_ebs_volume, expected_type=type_hints["managed_ebs_volume"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "managed_ebs_volume": managed_ebs_volume,
            "name": name,
        }

    @builtins.property
    def managed_ebs_volume(self) -> "EcsServiceVolumeConfigurationManagedEbsVolume":
        '''managed_ebs_volume block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#managed_ebs_volume EcsService#managed_ebs_volume}
        '''
        result = self._values.get("managed_ebs_volume")
        assert result is not None, "Required property 'managed_ebs_volume' is missing"
        return typing.cast("EcsServiceVolumeConfigurationManagedEbsVolume", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#name EcsService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceVolumeConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationManagedEbsVolume",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "encrypted": "encrypted",
        "file_system_type": "fileSystemType",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "size_in_gb": "sizeInGb",
        "snapshot_id": "snapshotId",
        "tag_specifications": "tagSpecifications",
        "throughput": "throughput",
        "volume_type": "volumeType",
    },
)
class EcsServiceVolumeConfigurationManagedEbsVolume:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        file_system_type: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        size_in_gb: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.
        :param encrypted: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#encrypted EcsService#encrypted}.
        :param file_system_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#file_system_type EcsService#file_system_type}.
        :param iops: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iops EcsService#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key_id EcsService#kms_key_id}.
        :param size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#size_in_gb EcsService#size_in_gb}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#snapshot_id EcsService#snapshot_id}.
        :param tag_specifications: tag_specifications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tag_specifications EcsService#tag_specifications}
        :param throughput: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#throughput EcsService#throughput}.
        :param volume_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_type EcsService#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e8fee625a9f1136afab20312cd0832b25f2f2a5484d6a546cd2f187d75caef9)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument file_system_type", value=file_system_type, expected_type=type_hints["file_system_type"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument tag_specifications", value=tag_specifications, expected_type=type_hints["tag_specifications"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if file_system_type is not None:
            self._values["file_system_type"] = file_system_type
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if size_in_gb is not None:
            self._values["size_in_gb"] = size_in_gb
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if tag_specifications is not None:
            self._values["tag_specifications"] = tag_specifications
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#encrypted EcsService#encrypted}.'''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def file_system_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#file_system_type EcsService#file_system_type}.'''
        result = self._values.get("file_system_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iops EcsService#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key_id EcsService#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#size_in_gb EcsService#size_in_gb}.'''
        result = self._values.get("size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#snapshot_id EcsService#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_specifications(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications"]]]:
        '''tag_specifications block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tag_specifications EcsService#tag_specifications}
        '''
        result = self._values.get("tag_specifications")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications"]]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#throughput EcsService#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_type EcsService#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceVolumeConfigurationManagedEbsVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceVolumeConfigurationManagedEbsVolumeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationManagedEbsVolumeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0799f16eb1070e24104d3fc12b425cdcff40406b09fcf367e7b6d1a7576f408)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTagSpecifications")
    def put_tag_specifications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a73aa6f7f083aef7149f9cd4215c30e2f4478d923efc38ae6d36512088eece0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTagSpecifications", [value]))

    @jsii.member(jsii_name="resetEncrypted")
    def reset_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypted", []))

    @jsii.member(jsii_name="resetFileSystemType")
    def reset_file_system_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileSystemType", []))

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetSizeInGb")
    def reset_size_in_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeInGb", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

    @jsii.member(jsii_name="resetTagSpecifications")
    def reset_tag_specifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagSpecifications", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(
        self,
    ) -> "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsList":
        return typing.cast("EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsList", jsii.get(self, "tagSpecifications"))

    @builtins.property
    @jsii.member(jsii_name="encryptedInput")
    def encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "encryptedInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemTypeInput")
    def file_system_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInGbInput")
    def size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagSpecificationsInput")
    def tag_specifications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications"]]], jsii.get(self, "tagSpecificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a4c044796cd50fc2076173dd4642b4c53c8a035c6e1abe237e65046dc38f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileSystemType")
    def file_system_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemType"))

    @file_system_type.setter
    def file_system_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df527e46de40a7f724f9cc683e0cd982326c5cb96b3d0a5bc836111ec2056ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31a73c0f1634b611474151f5d272e703ca9ce4ab5585a9755ec1e44fb1d8583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e31d40bbd2874aef18381f337be081a47af745710012f4b19d70c3c69138cd61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5b5556c6dad3c092fcae249e142200c020322bfb1807c94e30f5f0fc7d3e9f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec976111a785cbe28bc1e851257ca6004dfe7bed6006bff7732075be7ff15aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b1675343b96e807e22ffd2178e4d887fd9f0c51ab757220be68585291b5c2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23d9cc60ea74ea912dad8600efcac6cc0ed9cf93e6545e489148584ce77311a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c39de69dbe700adcf39c32c6db7f3bf910e42d57445f79985e7dc4c858d5424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume]:
        return typing.cast(typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3cd78f34f69f5eda65144bf3b292512cfce3f4e6f528e15456ffeb1e2fed66a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "propagate_tags": "propagateTags",
        "tags": "tags",
    },
)
class EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        propagate_tags: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param resource_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#resource_type EcsService#resource_type}.
        :param propagate_tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#propagate_tags EcsService#propagate_tags}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags EcsService#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7a6e6011447c030cfddde5f208b5c2fae7dba4a53f2e0000f5a1cc3dbd419d)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_type": resource_type,
        }
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#resource_type EcsService#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#propagate_tags EcsService#propagate_tags}.'''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tags EcsService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b088e260089e64d48429844baef47792a68391728c3ebca7ddafdd869d4d50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47247fcadab7797da112474d690e0b09496ee57b5bd1be6bb3b7f49b7fea6f63)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b60e73e9bafb0bc122f9640e32819435602675cb85b0003ff3b401d6b1264d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c201359d33dccd0c3b5b3541fa472f9fe34a049fe3c9b432f0619438be8c4c00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6015c3a2de7caab1eee36822e62ab14399c4713ea7ed105d3f4ecd53ae391b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb0ef60091369ed1b4dc46c9d455c53c8e24989f59f1bd895a734f081d8f090)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610cf0ef96bcb23db12c87fc6f88974396abdf4882e8b187f019c2e844563982)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPropagateTags")
    def reset_propagate_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagateTags", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="propagateTagsInput")
    def propagate_tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "propagateTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="propagateTags")
    def propagate_tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "propagateTags"))

    @propagate_tags.setter
    def propagate_tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff0689afbbb1423c6eb7f001f4562366a8b23b5c5b9ad1c74b2b67f111e1acbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagateTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6751124063c8e3af389c28d56974d2f1a43ed4e4e9184c921b5455f86595cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e200c8517ec3e3dbfbb73a169845970e9af3712e7ef04cae5008db257a69e21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8d7d112afad37fc63efb13ed47ee4057b9b63544e8034c4bb0eaed9322d8fe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceVolumeConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVolumeConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4066a3120afac5b685d13852427bf14a8e325993baaf350b151217897ef21de5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putManagedEbsVolume")
    def put_managed_ebs_volume(
        self,
        *,
        role_arn: builtins.str,
        encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        file_system_type: typing.Optional[builtins.str] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        size_in_gb: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.
        :param encrypted: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#encrypted EcsService#encrypted}.
        :param file_system_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#file_system_type EcsService#file_system_type}.
        :param iops: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#iops EcsService#iops}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#kms_key_id EcsService#kms_key_id}.
        :param size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#size_in_gb EcsService#size_in_gb}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#snapshot_id EcsService#snapshot_id}.
        :param tag_specifications: tag_specifications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#tag_specifications EcsService#tag_specifications}
        :param throughput: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#throughput EcsService#throughput}.
        :param volume_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#volume_type EcsService#volume_type}.
        '''
        value = EcsServiceVolumeConfigurationManagedEbsVolume(
            role_arn=role_arn,
            encrypted=encrypted,
            file_system_type=file_system_type,
            iops=iops,
            kms_key_id=kms_key_id,
            size_in_gb=size_in_gb,
            snapshot_id=snapshot_id,
            tag_specifications=tag_specifications,
            throughput=throughput,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putManagedEbsVolume", [value]))

    @builtins.property
    @jsii.member(jsii_name="managedEbsVolume")
    def managed_ebs_volume(
        self,
    ) -> EcsServiceVolumeConfigurationManagedEbsVolumeOutputReference:
        return typing.cast(EcsServiceVolumeConfigurationManagedEbsVolumeOutputReference, jsii.get(self, "managedEbsVolume"))

    @builtins.property
    @jsii.member(jsii_name="managedEbsVolumeInput")
    def managed_ebs_volume_input(
        self,
    ) -> typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume]:
        return typing.cast(typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume], jsii.get(self, "managedEbsVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f998ffe9b720f9aa022262a89ca608e57d2bbb9df4485947c91206866acfaa00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EcsServiceVolumeConfiguration]:
        return typing.cast(typing.Optional[EcsServiceVolumeConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EcsServiceVolumeConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0605b01fd54a9706c2f7cbeef0183c46d505b043bca592cb55efbe4cd86f98c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ecsService.EcsServiceVpcLatticeConfigurations",
    jsii_struct_bases=[],
    name_mapping={
        "port_name": "portName",
        "role_arn": "roleArn",
        "target_group_arn": "targetGroupArn",
    },
)
class EcsServiceVpcLatticeConfigurations:
    def __init__(
        self,
        *,
        port_name: builtins.str,
        role_arn: builtins.str,
        target_group_arn: builtins.str,
    ) -> None:
        '''
        :param port_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port_name EcsService#port_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.
        :param target_group_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#target_group_arn EcsService#target_group_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f27689c66bbb768d43dd86b865799dd15c84f7e30081c17168938353ac9b5ed)
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port_name": port_name,
            "role_arn": role_arn,
            "target_group_arn": target_group_arn,
        }

    @builtins.property
    def port_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#port_name EcsService#port_name}.'''
        result = self._values.get("port_name")
        assert result is not None, "Required property 'port_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#role_arn EcsService#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_group_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ecs_service#target_group_arn EcsService#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        assert result is not None, "Required property 'target_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsServiceVpcLatticeConfigurations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsServiceVpcLatticeConfigurationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVpcLatticeConfigurationsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6366c41db61f2bdc0310e8a87c1f981637718ca5757f1ae6ae55e19e7f9cee0e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EcsServiceVpcLatticeConfigurationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f800e05dfee2e36fc5363f57a1e13c47eec13ed4c683abd0dbafbefd76e943)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EcsServiceVpcLatticeConfigurationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad87ee6b55471444f5ffc8112534a8ec5c9de264f9af6ec2de8d44c44a851e51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f0e2169c87c43e4dddfa694bd5b8877c5ee1ff3002742d1519f478a7394d9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f27fe05d670e1b0a5503d7d024598530d0321ecc48c2a6806c000b17eaec13a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVpcLatticeConfigurations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVpcLatticeConfigurations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVpcLatticeConfigurations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__148d5b85a2eb9aa5f4935868abc59c36a800637281c86e53dfca6fc0e22fa328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class EcsServiceVpcLatticeConfigurationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ecsService.EcsServiceVpcLatticeConfigurationsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__359dafefcd48df3df2ac0d5e108ae554805a296fe249934ea15bcbc5af976ad2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57c20e8f11c6b8f7da90a875215af99986f9cc9c363e71be6171bd0d2a9cc23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68af2923d87ce3e4f1bf6d1d5d230ed508ea845e4aba93a9a9dcaadee2707292)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3f184b211fb8aa6b6ad24f1f2bdd59dc88514b1484b0147d210584454cd525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVpcLatticeConfigurations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVpcLatticeConfigurations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVpcLatticeConfigurations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16990a923fc82a6f2cbdd9f99667fc533e13153e3ef993cb5a3b6136ff7d95de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "EcsService",
    "EcsServiceAlarms",
    "EcsServiceAlarmsOutputReference",
    "EcsServiceCapacityProviderStrategy",
    "EcsServiceCapacityProviderStrategyList",
    "EcsServiceCapacityProviderStrategyOutputReference",
    "EcsServiceConfig",
    "EcsServiceDeploymentCircuitBreaker",
    "EcsServiceDeploymentCircuitBreakerOutputReference",
    "EcsServiceDeploymentController",
    "EcsServiceDeploymentControllerOutputReference",
    "EcsServiceLoadBalancer",
    "EcsServiceLoadBalancerList",
    "EcsServiceLoadBalancerOutputReference",
    "EcsServiceNetworkConfiguration",
    "EcsServiceNetworkConfigurationOutputReference",
    "EcsServiceOrderedPlacementStrategy",
    "EcsServiceOrderedPlacementStrategyList",
    "EcsServiceOrderedPlacementStrategyOutputReference",
    "EcsServicePlacementConstraints",
    "EcsServicePlacementConstraintsList",
    "EcsServicePlacementConstraintsOutputReference",
    "EcsServiceServiceConnectConfiguration",
    "EcsServiceServiceConnectConfigurationLogConfiguration",
    "EcsServiceServiceConnectConfigurationLogConfigurationOutputReference",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOption",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionList",
    "EcsServiceServiceConnectConfigurationLogConfigurationSecretOptionOutputReference",
    "EcsServiceServiceConnectConfigurationOutputReference",
    "EcsServiceServiceConnectConfigurationService",
    "EcsServiceServiceConnectConfigurationServiceClientAlias",
    "EcsServiceServiceConnectConfigurationServiceClientAliasOutputReference",
    "EcsServiceServiceConnectConfigurationServiceList",
    "EcsServiceServiceConnectConfigurationServiceOutputReference",
    "EcsServiceServiceConnectConfigurationServiceTimeout",
    "EcsServiceServiceConnectConfigurationServiceTimeoutOutputReference",
    "EcsServiceServiceConnectConfigurationServiceTls",
    "EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority",
    "EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthorityOutputReference",
    "EcsServiceServiceConnectConfigurationServiceTlsOutputReference",
    "EcsServiceServiceRegistries",
    "EcsServiceServiceRegistriesOutputReference",
    "EcsServiceTimeouts",
    "EcsServiceTimeoutsOutputReference",
    "EcsServiceVolumeConfiguration",
    "EcsServiceVolumeConfigurationManagedEbsVolume",
    "EcsServiceVolumeConfigurationManagedEbsVolumeOutputReference",
    "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications",
    "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsList",
    "EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecificationsOutputReference",
    "EcsServiceVolumeConfigurationOutputReference",
    "EcsServiceVpcLatticeConfigurations",
    "EcsServiceVpcLatticeConfigurationsList",
    "EcsServiceVpcLatticeConfigurationsOutputReference",
]

publication.publish()

def _typecheckingstub__37ac4570462af646dff8e915110fdf704bcbbf8a668ca7b90381d776cd581665(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    alarms: typing.Optional[typing.Union[EcsServiceAlarms, typing.Dict[builtins.str, typing.Any]]] = None,
    availability_zone_rebalancing: typing.Optional[builtins.str] = None,
    capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: typing.Optional[builtins.str] = None,
    deployment_circuit_breaker: typing.Optional[typing.Union[EcsServiceDeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_controller: typing.Optional[typing.Union[EcsServiceDeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_maximum_percent: typing.Optional[jsii.Number] = None,
    deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_new_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
    iam_role: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    network_configuration: typing.Optional[typing.Union[EcsServiceNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ordered_placement_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    scheduling_strategy: typing.Optional[builtins.str] = None,
    service_connect_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    service_registries: typing.Optional[typing.Union[EcsServiceServiceRegistries, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    task_definition: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[EcsServiceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    volume_configuration: typing.Optional[typing.Union[EcsServiceVolumeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_lattice_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVpcLatticeConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ed5de39cce407e6330cc852669606c2b7683017f4544f0ba9c7d12c35ea7a5(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b37cfccd18c498c53efcdb2611369b975d39b610f485b4d317f36633aa7909b7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c449529175f15b84c519472c936cf5ba5349e9e7c704bd92ecae94bac26e29(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea64e0b414c090e191490c9feef9e16231a98148e80fa8f2f27bc2da9f8c07d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb1b694c4aba723ecac977a43c9021e5d74d164d31da946e8e006da012a2e4f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a263d883acebe332c84ff454abcc5bd48c8595b25c44190f2bd8c4d741ea5a5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVpcLatticeConfigurations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33305a2f2c8ca9caa8f36c801cadc950a272351dc4f7b8b1cb708587bcfafcad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2049343789f7180c210b28c083910dfb0a5ff1e951feca6f301fb0f925e5be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da20988d2dd298506a27c1aa51fdf24775ba02724bea0a5962772ca96825cbd0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f54c2146f0640c54f92e6142ed177bfb5fb8fdd13619bde74c4dfa812741c85b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910f5a1202dadf5d0c15c5f36da0b379fb1bca3797de3eb73e88844c22249f2a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313ca990559bcccf24f893ee690453cc43ad106b3b7e48d59c3c8b4c700db841(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78625708600bcbfb0c363a05f29bb8c0bedd6bc6561949b317404323ca4cd943(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66718fe220b73f4154b8444a3b98b93d199d32293b5e7aa902d6b532fcb31b2b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2b078d0f08e2266596151772d62fb9bcb17eb921a928df6d842d7d5859f3df(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ee43554adc07ff10ac9b55211a79ad652242f8e7eac995b4602d662181b3a5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0e00c0dc5d9997cfc13fe72497408334629b8d066395ae68149fe8c7f5b557(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05f53d472fcb637248e39fd0ab1f6d076ea4127ff138e440378fedc56e2dfac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e38435cf7350eed6c7e6e5476d1f87db4b9fedfac66514789c033e9d0d4cf02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302e5f86c9052279ddb7c78bb30b9fd0c32cc72bad621dd82cc36ea01ca97512(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd51c44bf2d1fb3c8366748b8e6967e7486f4989ba60a4805a5424a1a6d091e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc05eb18dc6623b3cebb8f2685ebde9464fae64afedf3bacdb61e934fa6c34f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a9ec79be7e01d024ccf014d31c9ff208fa333437448146e697f034db49192b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55211370165051b256052bfa2b1b9ffdaafdbeb293a910b775af54baa79c44a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aaa903c9afca983406363695cfeeab75eb558a2722a77f7c74e006fc3c27a48(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0df3d383ead5ef1bcfa4e98465e241e4137851c21cb0ef0c4638b9a0b89e23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__700df6a613fd246ccd59966356c822a147217b170ad3ff7d0a916584c89b0597(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04de3a1313b5583f7e983d2947584c05b3f667965d67401eaa578cb34f1094b6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0236b72b4c3632c5de55dec2520561f5520f31719d92c0f0dc1e0bb01cc5c193(
    *,
    alarm_names: typing.Sequence[builtins.str],
    enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb647e1ae084c86b146c9255210611a51bd5686ead9ec2f0aa44810a6a8cc8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b097a464b6698b8d453b0c14882c820b737ab600ddf134c022f94e8fcfd31e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4de458c0af050856fc66146999086628f2292588e42ee8bc47c648fc9702917(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b1793961eac5e9ce3496f2681259b8c982838a9408c58d990e56dd4aef1490(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652c3f22a2ace725ac8ac077c128adee3e25cfe361370ca8f995bcc0b1b7fdc1(
    value: typing.Optional[EcsServiceAlarms],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e17a106ff1da4d1f5d9ae25ba4ea4b0a8da3f320ed8d054c999e5d6108dfc83e(
    *,
    capacity_provider: builtins.str,
    base: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690499275c4fde2c17194624fad9a4119decd1b3e5b8bccde02515b10d005378(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3216f9b65c08d77c9cd0cd5c6d2bba838bfdf6b032cf29affded023c885d031c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad1bdc38d32f15301e03afe1f969da8bc57d94919116f405b5248af9cd41ae56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a91f5ead406b5180f8e5109a5bb3c8d24745f38ead09896308a5193cdd90565(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05fba52eb23c1e5b8b2a5ea47ce2983fccbe54285fb5ef906668ccf895270889(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072f99cf4f6a9f7d9c913bfe4bc414f14a2c09915956abe178bbd4fc030b79d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceCapacityProviderStrategy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d49960a5c1adb0ea66b1ea16234abdb21c2ad4b6ca9d5ebb9d0967dbc870f3c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa5a5783519b5c93e666213ff7d28115b62e97647f12311a114bfb9f7077c28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0da3f59eb5e8ec9b11241fa93ae7829fa93b2eff6221c686c70cf13fda805fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49cca3312b5355bf429fddba1d45f18b6d53181f689e1702aa0cfa31edfc1002(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c9878fbdd64103f4c6e2ccd46ab6341367f6ba76731f892ad100fc11b8463d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceCapacityProviderStrategy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd06227334c2f29835ac4df8c10ce828d0382b9a4135d3f943ec5d04d412568(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    alarms: typing.Optional[typing.Union[EcsServiceAlarms, typing.Dict[builtins.str, typing.Any]]] = None,
    availability_zone_rebalancing: typing.Optional[builtins.str] = None,
    capacity_provider_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceCapacityProviderStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: typing.Optional[builtins.str] = None,
    deployment_circuit_breaker: typing.Optional[typing.Union[EcsServiceDeploymentCircuitBreaker, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_controller: typing.Optional[typing.Union[EcsServiceDeploymentController, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_maximum_percent: typing.Optional[jsii.Number] = None,
    deployment_minimum_healthy_percent: typing.Optional[jsii.Number] = None,
    desired_count: typing.Optional[jsii.Number] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_delete: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    force_new_deployment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    health_check_grace_period_seconds: typing.Optional[jsii.Number] = None,
    iam_role: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    load_balancer: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceLoadBalancer, typing.Dict[builtins.str, typing.Any]]]]] = None,
    network_configuration: typing.Optional[typing.Union[EcsServiceNetworkConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    ordered_placement_strategy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceOrderedPlacementStrategy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    placement_constraints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServicePlacementConstraints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    scheduling_strategy: typing.Optional[builtins.str] = None,
    service_connect_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    service_registries: typing.Optional[typing.Union[EcsServiceServiceRegistries, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    task_definition: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[EcsServiceTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    triggers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    volume_configuration: typing.Optional[typing.Union[EcsServiceVolumeConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_lattice_configurations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVpcLatticeConfigurations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wait_for_steady_state: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd544fef19ed11253d9f4d8f7cc38ce853204dd3d738f660413d9c0fb3dfcce(
    *,
    enable: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    rollback: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fb61a0e890a8c246b7b37f43ae2158e533ff96dd1d55ebbbc8f9ad6635b387(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525eada7d1b28b6625022f9e967e80f9b9ff92a493632c0c8ba805070cc4949a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443e6f1767f767022d0bc5727875f4b274f671a86d0e9176619e6ce68513a34c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__426c0d62a39fe666930412c7ac47957a69329df70bbeb25b3c6097c4b4aef303(
    value: typing.Optional[EcsServiceDeploymentCircuitBreaker],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c734efd8ce7f47bf93f561d582cb059d1826da611c2844fc62ff8415073e278(
    *,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b384797f044bfc97b63fc8e7e752475c3181b1dade08d76b75467db2b6f6851f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e20f5bfff0c215b8e41f581972b615856787c18dd4765f80ddfed8bbd4e7bd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7851c942aec497e92e5c2469e10e6d4a87349879297c8771b4e92135bd7de1(
    value: typing.Optional[EcsServiceDeploymentController],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43301010cd18d6073ed4b6f5f536641ad5625729ee1d9f32d5ea87d03e27254(
    *,
    container_name: builtins.str,
    container_port: jsii.Number,
    elb_name: typing.Optional[builtins.str] = None,
    target_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53c2eeceeee0fe93db6e9bfd209ff4bd5cb20388ccd44e3e61f7da9d5f51a19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41ead0c9e9e9de74ad556b1a3c02eb7bc64e222f0c896989b5b111f4a7a91df3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154fdd5c7b2ac7da2fb93c260e7e037b313ff71baa7353e2e4e7dfd571b112f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dcaefa87b4d925355bbf9cded6b7249c77fa6e5d7153a992e8f00b2faeb0066(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__364853fc608744c8683c4fd01b774bd28d57b42625f3fce6367c8c9035a5e963(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3b21d60b0b42f25493b9ac64e8e02dff80a3da53cd71ad46a9d050747b2319(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceLoadBalancer]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17492237fd499c46c35dd4ffb1d0d2ed0826481c6fb762408777920b22269816(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59590190fd6e4c85afeb6ccefa1680e67cd20d159ed936e47a1751c9f6af6c57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31261925bf84f447136d44a1c724bdf810b35124e3901f541a1bd84ee8699e77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccef3159d41aee6d6e50dcc6abf5ae9b53f97303a88bc4503f25fce0f0296cc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe424d03bdbadb2b1f37dfb265be0985d9e3dd905aeef7368c9b46173a7930f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790b1e1ab99900de908b6f7691afa448396ef46e98c2eede9b3dd1bf25819186(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceLoadBalancer]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e6cc44d9afd037522d6dd54e09e5f1f58098dbacc3ff1b665bcf53bc443d74(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4165cc3e809d5f2017474531df70935454aafba146dcc1b1f65402b854ab84cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06521eed398e5449af9731c85f59146082134ee4e921d06edcd835a99724da19(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b01d8f6d390d8b7e9f5169f74bf59770f9154f337069839cc98bd6da43b3326d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c5d035ae2ec4256e9259ca5df2b41875484e6fecdee0250e3f05c0201c2e7c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e69498fe504da84ec958188e5e1e6aafc4246b8105076aeb521bf73f1da693(
    value: typing.Optional[EcsServiceNetworkConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b2fa02c5ee0700f3450427062fbfa1178032fce4ed5897958d2112e5df0e2d0(
    *,
    type: builtins.str,
    field: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6fb2f946b7987282e5b0b857c03ba822a5c1e659705a01f23d436dc0f2eaf8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e0c042bc787756d8163d70ba79ab5c9191bb251a8a0baa978b48d5f0395188(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8388444d4b284fc348c59328cd0f8fe4e78df0c4e8ee9ea63af82c778a86c0d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b637f7cf479016698612bf153359a5663b91110267b39da1b3b7f61c60981845(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ca22af699247f311c781f495c69532c31ab0ad8f234e6f3ef73d71b7430151(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf5e4205d6fd99c86e8cce51da0dfd03f89d615d293006587290f5cb96a213c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceOrderedPlacementStrategy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b36da589f0e632ecae9266be8f8b1b2233952f052f07e3c3250a136dbdd7a0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f847ebc948cbab0441e4037ee8aec3c1590f7d3b82dd920a03a078bf9cc24c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1363e51f54f40bf5732d0299c347c3139e709e45eb935ed797579f7011de95f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4dd7d1a769de9b0dfb5f5a378fe4f958ae89fd1242de2f85439a604b7ed223e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceOrderedPlacementStrategy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca6dead5764b3362f489002ae19f9df8369566a8e660c320d82fe37eb7fa5a0(
    *,
    type: builtins.str,
    expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc635750032622d26096a7358537cca9b8699aa3d5088221586e14f4c8f9b64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__899b506235dce009d82ad235e82b6b907703a8390f77397ffdd7f750bb36a2f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e9aeea76170bb7f6eb39faaca77c47c2f8524c0973e2f091eec8d3b2397241(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f1836da08448d685e37fc37d7ec63a8d33bffa7c7905badd5f5b806bfd3e63(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d33fcead1c9627f5ec752c30132fbb3d4ea07904ec87d14b4c6f9ca322019af(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e554fdfac315791a20270262edeb994b329a22082eb5d7b777454b8fe7e83f08(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServicePlacementConstraints]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f69f23c62b4276d4f78ab0b218cf7d4f24c946a24c9bbe70a4fa035d97f929(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00b130d3a60a3a3467defb1c63e4066a2d009782650fbc521f26c805942d84df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4daaa45b89e7f33994d222113202dfd0c6857704404f7d3ea67296052888f7ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33f45c4f20c8586666e1ac40630fd774dc4a0b3ace5505711e86ab66fa6f4705(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServicePlacementConstraints]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a36c700ffce96721bb674a30a401e035df2f3da4a64a8440ea1610bfc704b3a(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    log_configuration: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationLogConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    namespace: typing.Optional[builtins.str] = None,
    service: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationService, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b994ea1dfb29104d881f1785df924404392b77f02d6747bd98f9f59ea4000c6f(
    *,
    log_driver: builtins.str,
    options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    secret_option: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a3f5b4700e5df9dd52665c77bec31b0aaba4ee9d67fd6a6d5487e80e0e8125(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739a5eb9090eb5a505d7344b4e04c376ef0d8ac69b54836717c5918ff5910a92(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a85d40e624ec67f7a7e6e9332f2b62d43c3e6bcdd5f75473ad13dd77beffbfcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dabaa670e16c08e2b56d7c81ca20b479f0b6a6f70af5232fa5522f803eca6b5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff1a15e5b7032e945228317440d554206140bbcdef9441a4d9b27ce974ae5f80(
    value: typing.Optional[EcsServiceServiceConnectConfigurationLogConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d601e6b26d92ec645e67f0df4877eee7511694d3555f9812e6e7b581a4b150f(
    *,
    name: builtins.str,
    value_from: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38bf5c3c786c2e131802a8d15ed391f74fd5453b7e5303fcf73aaaf8ff99f738(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fea7bf5eb8e8ad1b39ecd5afac52b0272242c523ae743e90eb6463dbb506c34(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391596afcb6da7cc10b1091820ba3e9f2b315c3a2365f9e6f298d183a12e79af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffefa7580b4d5f396a09195cffb8834e9b6ae30d598fee794af1fc10347ee54a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097caf2df780bedc54752fcc54bcf18a1f87cfe57827137cec3f1bd5f6a6c1b6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35dac268da65f166b0003d9ca1e6c9b697b072522d52119cff112607c06d05f4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f0b2ed23fac04d1144233eeaedda55483d6ac0857470e8bac00e6c81f2c670(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a86556f7df913e54df08a6e4ccf21a7072b2715cadb5000bff1d0fde81cea8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7970a829314cf79027952be4a6d5127b594607b5e264d7a33c4232c227c840(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0541c8e2191396bb7378436b9cadfcb649bf8c4badc4ca90750dc7dc8614402c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationLogConfigurationSecretOption]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d005cfcdb7408ad8d4650db266c9b91260f5cfd6d744caa6168c9616bac9f523(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92aa69acd12070b1561de0490e8c790c09327b3ecc011cf29eae28025f79ae60(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceServiceConnectConfigurationService, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__840f9603b0b3c67930ed47e8082be1f5f3a682cbc9995ac5229a6a12ca35b365(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7619f9f8cc023211abb9d0c3a27df69b217e6d7068e2bb9dc682e5653d6a380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59bcdc329a7616fb4108ac0c0748e198659147134420a0b469db2745619ee6f2(
    value: typing.Optional[EcsServiceServiceConnectConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393fa0a93131289bc28987cc899fb914f3b9a3f15c6a5e077275b46c5b30e394(
    *,
    port_name: builtins.str,
    client_alias: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceClientAlias, typing.Dict[builtins.str, typing.Any]]] = None,
    discovery_name: typing.Optional[builtins.str] = None,
    ingress_port_override: typing.Optional[jsii.Number] = None,
    timeout: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    tls: typing.Optional[typing.Union[EcsServiceServiceConnectConfigurationServiceTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd09bd41bb46ea4f2e707299517224725fadff30ec2321ea22dad3d495f9c5f(
    *,
    port: jsii.Number,
    dns_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53966912423f8d25c38414fa638067ec8798cc99a272bc15ae8920a2d66f1bdf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300650857892dfa4c099a739254f648e0a962abca0da4b8a57f1d348402fd9b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ce1a8b0f4531ab7b405ec614be289beae16279c7b00bd7172e5d72f86ea1e36(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1006bfa48d8e2e637f13214e6f3ee22c1d176fdc1a1c199b79d1c4369b816ff(
    value: typing.Optional[EcsServiceServiceConnectConfigurationServiceClientAlias],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__051417a6d80dba73e39f14156ec15547f316ae677bcffba32f32e744284132c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dfcb25f9262a528231d260c2ff59e964a82757dad71eb6acf9fca2c54897ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b28b236a23932aeb6f20501bc6ed14000d376bbb3ea4203769f3c6e03a78c503(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e8f8370d26e0bef4d2c4bbf1294c76eab3e693756873876c99b01c60fbf74f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81a261a8d520412090c15e847777da7ebfd839b1eb98845e2a01163549b1574(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62bec76c00b51e254290fc53d44852de3bd6dbb3ed69dd0dc0e5a01f37122c31(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceServiceConnectConfigurationService]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c6e8dd21747629f4aa425e2b7457d90a2952da373309934f00a9ffa8a102ef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22160f5404a257b6ab47eaa563c56d713250a4b7a63e1a4ec0701dd55c073f30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e114371bec53e5eebab53b7a5277d7d26cded1fd56f10c6bee2a5437354bf80c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec443c3482179e5d719595dfc2bf664f56834dd4274dfa116843ba07e3fc76b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e1233b63434dce3afebdbfd049698487d0539f90a3c7c1b83419f66ce7f1130(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceServiceConnectConfigurationService]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3b919fad4722129f59b1d91f451b54dfaec4e1ad11b12b1ba0389ee2151ce4(
    *,
    idle_timeout_seconds: typing.Optional[jsii.Number] = None,
    per_request_timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67614d8cd89acc79cd9869dda5b1e246930270c352b4909e0ba7ec995369400(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b8e36a07cc839b6de4db59dd5b3cb450621a7d6f6e2fba9a0bd655aa9b7832(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0a991877fb607d539ea50ad38d286fa3a3a7ba60c93303fafaa9b00c0958aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffcae1dae1e4f494f00f73ac8870a7f1227c1c267ce2f740d816444074952c3d(
    value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129cbd0cf3a568863742a0434cbf5a99af649a91e66358679f3df08cbe477e7f(
    *,
    issuer_cert_authority: typing.Union[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority, typing.Dict[builtins.str, typing.Any]],
    kms_key: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__628b293eece7db44f48da69f72256ea536a0e0c5db7db5469c04d73f3c50d452(
    *,
    aws_pca_authority_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa902297f7a8eff9c46e0bddee7191b591bd4a32d8a7a1465a99e70428e36ff1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__761aecb98886ea91e8a89b05580b954f7edad343290e0eb17edd9b3bb612e254(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802b5cb710914afbd784878dd3a1f06c888fadca6d2dba40d328a2213cd8f583(
    value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTlsIssuerCertAuthority],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a947dfde7a9d26d740fd570a082371a5228f526d13e5f100201867c1330d24e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4079b4b254cdb3adecd85138c2d1cdac505a72b88b60250b3fc34ede13652c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253074588ab89f3de6140a21237b42b500d78766000bc879af2a8d3ee7632222(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044bded658d1c6f3976747ae4f1aa01123dd07c96909eb1dd739b2dd6560209a(
    value: typing.Optional[EcsServiceServiceConnectConfigurationServiceTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4100c9e3181d870eb2e7c717677a77b5720df463be07499b88a2e88f9a84d747(
    *,
    registry_arn: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    container_port: typing.Optional[jsii.Number] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982993001259ee192b695778f2d921d0f1ebe01b16b90301854fadbc49f9f6dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f8f13d84b0f0a57cb0e0037c51a16c19d5c989702f2ed9f217b8686a3e1ea3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb32577796872f39d9c727f67541066c8b450a81f0792b1ae807f7068d42ac2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a71be5c7524b3fa68e74a9ba9f65c373510ecbafa39cb6ed76dbdb79baf3d2d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ee5b6863ff387d7572995061a3a10d42128c66033ba591f26d1513034b6bf5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1fdf4414cd92685ab943ea669922022d881ff458252825962b233941d79dfc(
    value: typing.Optional[EcsServiceServiceRegistries],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e692230dc0dcb4d24210eac41f91326cb0ff028aa64838e480d23d8549d43fc(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b837eb063f394c219ec80fa8e46375df1158321e903bcb367cdd5a100da81ba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056bd135dc818617b99c74060604c439ccddd136f96152404d0a0dbac0dcf16d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81196a834f5ba4bf4b6e25b5b3a1aa94df1a68e0c2fa65c2a6882ef05f00835d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734dba84c459351bcca614fb68fde308747b0c0864ee9ebf58e19d4609e7f673(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed87d28341b67076c9dec1d8cf79a1d3ef92432f857274b6024e5be34916ce9b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceTimeouts]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6911ab88651a2ab29d5dcf6aa67a78707c0e09f6fc9d846ccbf2286f6139cb8(
    *,
    managed_ebs_volume: typing.Union[EcsServiceVolumeConfigurationManagedEbsVolume, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8fee625a9f1136afab20312cd0832b25f2f2a5484d6a546cd2f187d75caef9(
    *,
    role_arn: builtins.str,
    encrypted: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    file_system_type: typing.Optional[builtins.str] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    size_in_gb: typing.Optional[jsii.Number] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    tag_specifications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0799f16eb1070e24104d3fc12b425cdcff40406b09fcf367e7b6d1a7576f408(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a73aa6f7f083aef7149f9cd4215c30e2f4478d923efc38ae6d36512088eece0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a4c044796cd50fc2076173dd4642b4c53c8a035c6e1abe237e65046dc38f05(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df527e46de40a7f724f9cc683e0cd982326c5cb96b3d0a5bc836111ec2056ed2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31a73c0f1634b611474151f5d272e703ca9ce4ab5585a9755ec1e44fb1d8583(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31d40bbd2874aef18381f337be081a47af745710012f4b19d70c3c69138cd61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5b5556c6dad3c092fcae249e142200c020322bfb1807c94e30f5f0fc7d3e9f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec976111a785cbe28bc1e851257ca6004dfe7bed6006bff7732075be7ff15aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b1675343b96e807e22ffd2178e4d887fd9f0c51ab757220be68585291b5c2e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23d9cc60ea74ea912dad8600efcac6cc0ed9cf93e6545e489148584ce77311a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c39de69dbe700adcf39c32c6db7f3bf910e42d57445f79985e7dc4c858d5424(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3cd78f34f69f5eda65144bf3b292512cfce3f4e6f528e15456ffeb1e2fed66a(
    value: typing.Optional[EcsServiceVolumeConfigurationManagedEbsVolume],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7a6e6011447c030cfddde5f208b5c2fae7dba4a53f2e0000f5a1cc3dbd419d(
    *,
    resource_type: builtins.str,
    propagate_tags: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b088e260089e64d48429844baef47792a68391728c3ebca7ddafdd869d4d50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47247fcadab7797da112474d690e0b09496ee57b5bd1be6bb3b7f49b7fea6f63(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b60e73e9bafb0bc122f9640e32819435602675cb85b0003ff3b401d6b1264d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c201359d33dccd0c3b5b3541fa472f9fe34a049fe3c9b432f0619438be8c4c00(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6015c3a2de7caab1eee36822e62ab14399c4713ea7ed105d3f4ecd53ae391b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb0ef60091369ed1b4dc46c9d455c53c8e24989f59f1bd895a734f081d8f090(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610cf0ef96bcb23db12c87fc6f88974396abdf4882e8b187f019c2e844563982(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff0689afbbb1423c6eb7f001f4562366a8b23b5c5b9ad1c74b2b67f111e1acbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6751124063c8e3af389c28d56974d2f1a43ed4e4e9184c921b5455f86595cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e200c8517ec3e3dbfbb73a169845970e9af3712e7ef04cae5008db257a69e21(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8d7d112afad37fc63efb13ed47ee4057b9b63544e8034c4bb0eaed9322d8fe1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVolumeConfigurationManagedEbsVolumeTagSpecifications]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4066a3120afac5b685d13852427bf14a8e325993baaf350b151217897ef21de5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f998ffe9b720f9aa022262a89ca608e57d2bbb9df4485947c91206866acfaa00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0605b01fd54a9706c2f7cbeef0183c46d505b043bca592cb55efbe4cd86f98c4(
    value: typing.Optional[EcsServiceVolumeConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f27689c66bbb768d43dd86b865799dd15c84f7e30081c17168938353ac9b5ed(
    *,
    port_name: builtins.str,
    role_arn: builtins.str,
    target_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6366c41db61f2bdc0310e8a87c1f981637718ca5757f1ae6ae55e19e7f9cee0e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f800e05dfee2e36fc5363f57a1e13c47eec13ed4c683abd0dbafbefd76e943(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad87ee6b55471444f5ffc8112534a8ec5c9de264f9af6ec2de8d44c44a851e51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f0e2169c87c43e4dddfa694bd5b8877c5ee1ff3002742d1519f478a7394d9b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f27fe05d670e1b0a5503d7d024598530d0321ecc48c2a6806c000b17eaec13a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148d5b85a2eb9aa5f4935868abc59c36a800637281c86e53dfca6fc0e22fa328(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EcsServiceVpcLatticeConfigurations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__359dafefcd48df3df2ac0d5e108ae554805a296fe249934ea15bcbc5af976ad2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57c20e8f11c6b8f7da90a875215af99986f9cc9c363e71be6171bd0d2a9cc23(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68af2923d87ce3e4f1bf6d1d5d230ed508ea845e4aba93a9a9dcaadee2707292(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3f184b211fb8aa6b6ad24f1f2bdd59dc88514b1484b0147d210584454cd525(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16990a923fc82a6f2cbdd9f99667fc533e13153e3ef993cb5a3b6136ff7d95de(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, EcsServiceVpcLatticeConfigurations]],
) -> None:
    """Type checking stubs"""
    pass
