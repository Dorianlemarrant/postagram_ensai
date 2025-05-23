r'''
# `aws_ssoadmin_permissions_boundary_attachment`

Refer to the Terraform Registry for docs: [`aws_ssoadmin_permissions_boundary_attachment`](https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment).
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


class SsoadminPermissionsBoundaryAttachment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachment",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment aws_ssoadmin_permissions_boundary_attachment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_arn: builtins.str,
        permissions_boundary: typing.Union["SsoadminPermissionsBoundaryAttachmentPermissionsBoundary", typing.Dict[builtins.str, typing.Any]],
        permission_set_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SsoadminPermissionsBoundaryAttachmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment aws_ssoadmin_permissions_boundary_attachment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#instance_arn SsoadminPermissionsBoundaryAttachment#instance_arn}.
        :param permissions_boundary: permissions_boundary block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permissions_boundary SsoadminPermissionsBoundaryAttachment#permissions_boundary}
        :param permission_set_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permission_set_arn SsoadminPermissionsBoundaryAttachment#permission_set_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#id SsoadminPermissionsBoundaryAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#timeouts SsoadminPermissionsBoundaryAttachment#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac360cbd595af5e5d17df342c3b75f2af1ea72f0cd85212cfd58319df8dee3c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SsoadminPermissionsBoundaryAttachmentConfig(
            instance_arn=instance_arn,
            permissions_boundary=permissions_boundary,
            permission_set_arn=permission_set_arn,
            id=id,
            timeouts=timeouts,
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
        '''Generates CDKTF code for importing a SsoadminPermissionsBoundaryAttachment resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the SsoadminPermissionsBoundaryAttachment to import.
        :param import_from_id: The id of the existing SsoadminPermissionsBoundaryAttachment that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the SsoadminPermissionsBoundaryAttachment to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646965b641b39312d4eb2b6657f2360563c60152ee6ebee75fa785137adf482a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putPermissionsBoundary")
    def put_permissions_boundary(
        self,
        *,
        customer_managed_policy_reference: typing.Optional[typing.Union["SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_policy_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param customer_managed_policy_reference: customer_managed_policy_reference block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#customer_managed_policy_reference SsoadminPermissionsBoundaryAttachment#customer_managed_policy_reference}
        :param managed_policy_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#managed_policy_arn SsoadminPermissionsBoundaryAttachment#managed_policy_arn}.
        '''
        value = SsoadminPermissionsBoundaryAttachmentPermissionsBoundary(
            customer_managed_policy_reference=customer_managed_policy_reference,
            managed_policy_arn=managed_policy_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putPermissionsBoundary", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#create SsoadminPermissionsBoundaryAttachment#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#delete SsoadminPermissionsBoundaryAttachment#delete}.
        '''
        value = SsoadminPermissionsBoundaryAttachmentTimeouts(
            create=create, delete=delete
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> "SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryOutputReference":
        return typing.cast("SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryOutputReference", jsii.get(self, "permissionsBoundary"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "SsoadminPermissionsBoundaryAttachmentTimeoutsOutputReference":
        return typing.cast("SsoadminPermissionsBoundaryAttachmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceArnInput")
    def instance_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundaryInput")
    def permissions_boundary_input(
        self,
    ) -> typing.Optional["SsoadminPermissionsBoundaryAttachmentPermissionsBoundary"]:
        return typing.cast(typing.Optional["SsoadminPermissionsBoundaryAttachmentPermissionsBoundary"], jsii.get(self, "permissionsBoundaryInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionSetArnInput")
    def permission_set_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionSetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "SsoadminPermissionsBoundaryAttachmentTimeouts"]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, "SsoadminPermissionsBoundaryAttachmentTimeouts"]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfd0f298accca344aab081ecc144c9367d15a0af586d631ca1009f792cf9325e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d26171e06c7058891aff3b2d9c935d91ad1d4f292bce62bd871662176a44f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="permissionSetArn")
    def permission_set_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionSetArn"))

    @permission_set_arn.setter
    def permission_set_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e518989dbe576baaa9f2f96fe0a8697ab09a1947ca776fb1cb2584541f5103c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionSetArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_arn": "instanceArn",
        "permissions_boundary": "permissionsBoundary",
        "permission_set_arn": "permissionSetArn",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class SsoadminPermissionsBoundaryAttachmentConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        instance_arn: builtins.str,
        permissions_boundary: typing.Union["SsoadminPermissionsBoundaryAttachmentPermissionsBoundary", typing.Dict[builtins.str, typing.Any]],
        permission_set_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SsoadminPermissionsBoundaryAttachmentTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param instance_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#instance_arn SsoadminPermissionsBoundaryAttachment#instance_arn}.
        :param permissions_boundary: permissions_boundary block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permissions_boundary SsoadminPermissionsBoundaryAttachment#permissions_boundary}
        :param permission_set_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permission_set_arn SsoadminPermissionsBoundaryAttachment#permission_set_arn}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#id SsoadminPermissionsBoundaryAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#timeouts SsoadminPermissionsBoundaryAttachment#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(permissions_boundary, dict):
            permissions_boundary = SsoadminPermissionsBoundaryAttachmentPermissionsBoundary(**permissions_boundary)
        if isinstance(timeouts, dict):
            timeouts = SsoadminPermissionsBoundaryAttachmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ca0d766a63e1d730571d412526a5be94ca8ba42a57ee63d90ddfdc59bbd9fb2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "permissions_boundary": permissions_boundary,
            "permission_set_arn": permission_set_arn,
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
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def instance_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#instance_arn SsoadminPermissionsBoundaryAttachment#instance_arn}.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permissions_boundary(
        self,
    ) -> "SsoadminPermissionsBoundaryAttachmentPermissionsBoundary":
        '''permissions_boundary block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permissions_boundary SsoadminPermissionsBoundaryAttachment#permissions_boundary}
        '''
        result = self._values.get("permissions_boundary")
        assert result is not None, "Required property 'permissions_boundary' is missing"
        return typing.cast("SsoadminPermissionsBoundaryAttachmentPermissionsBoundary", result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#permission_set_arn SsoadminPermissionsBoundaryAttachment#permission_set_arn}.'''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#id SsoadminPermissionsBoundaryAttachment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["SsoadminPermissionsBoundaryAttachmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#timeouts SsoadminPermissionsBoundaryAttachment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SsoadminPermissionsBoundaryAttachmentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsoadminPermissionsBoundaryAttachmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentPermissionsBoundary",
    jsii_struct_bases=[],
    name_mapping={
        "customer_managed_policy_reference": "customerManagedPolicyReference",
        "managed_policy_arn": "managedPolicyArn",
    },
)
class SsoadminPermissionsBoundaryAttachmentPermissionsBoundary:
    def __init__(
        self,
        *,
        customer_managed_policy_reference: typing.Optional[typing.Union["SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference", typing.Dict[builtins.str, typing.Any]]] = None,
        managed_policy_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param customer_managed_policy_reference: customer_managed_policy_reference block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#customer_managed_policy_reference SsoadminPermissionsBoundaryAttachment#customer_managed_policy_reference}
        :param managed_policy_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#managed_policy_arn SsoadminPermissionsBoundaryAttachment#managed_policy_arn}.
        '''
        if isinstance(customer_managed_policy_reference, dict):
            customer_managed_policy_reference = SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference(**customer_managed_policy_reference)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f158c814e3852c3a83bf5e200f730a4b2d1996f8d8c3b35e758ce06e0e3b92c5)
            check_type(argname="argument customer_managed_policy_reference", value=customer_managed_policy_reference, expected_type=type_hints["customer_managed_policy_reference"])
            check_type(argname="argument managed_policy_arn", value=managed_policy_arn, expected_type=type_hints["managed_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if customer_managed_policy_reference is not None:
            self._values["customer_managed_policy_reference"] = customer_managed_policy_reference
        if managed_policy_arn is not None:
            self._values["managed_policy_arn"] = managed_policy_arn

    @builtins.property
    def customer_managed_policy_reference(
        self,
    ) -> typing.Optional["SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference"]:
        '''customer_managed_policy_reference block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#customer_managed_policy_reference SsoadminPermissionsBoundaryAttachment#customer_managed_policy_reference}
        '''
        result = self._values.get("customer_managed_policy_reference")
        return typing.cast(typing.Optional["SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference"], result)

    @builtins.property
    def managed_policy_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#managed_policy_arn SsoadminPermissionsBoundaryAttachment#managed_policy_arn}.'''
        result = self._values.get("managed_policy_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsoadminPermissionsBoundaryAttachmentPermissionsBoundary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path"},
)
class SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#name SsoadminPermissionsBoundaryAttachment#name}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#path SsoadminPermissionsBoundaryAttachment#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__526b8ca0830dcad2eb969465fb9c00d6d30e6ee5a88170e7e328c755e01195ea)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#name SsoadminPermissionsBoundaryAttachment#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#path SsoadminPermissionsBoundaryAttachment#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3934d77e7876e2173861436ce821725a0c8eb18bbf7166d6667997a5fb941a0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__000f8afbb24d65e2b7af5aa65faa39ef7b74d219afbd1b641b2ac448f4bd58da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__451692c76bce0eb5ae2068a4765c79bb68715906ef480693b0dd0027033afd0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference]:
        return typing.cast(typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__803ffb4f90892f3c9cc4b36d72453240add7316c6bdee4e0d7a1860dde913648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__418768da61581982c6c71f530fcc5a10be0b273465e22057211812970289a23e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomerManagedPolicyReference")
    def put_customer_managed_policy_reference(
        self,
        *,
        name: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#name SsoadminPermissionsBoundaryAttachment#name}.
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#path SsoadminPermissionsBoundaryAttachment#path}.
        '''
        value = SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference(
            name=name, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putCustomerManagedPolicyReference", [value]))

    @jsii.member(jsii_name="resetCustomerManagedPolicyReference")
    def reset_customer_managed_policy_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomerManagedPolicyReference", []))

    @jsii.member(jsii_name="resetManagedPolicyArn")
    def reset_managed_policy_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedPolicyArn", []))

    @builtins.property
    @jsii.member(jsii_name="customerManagedPolicyReference")
    def customer_managed_policy_reference(
        self,
    ) -> SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceOutputReference:
        return typing.cast(SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceOutputReference, jsii.get(self, "customerManagedPolicyReference"))

    @builtins.property
    @jsii.member(jsii_name="customerManagedPolicyReferenceInput")
    def customer_managed_policy_reference_input(
        self,
    ) -> typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference]:
        return typing.cast(typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference], jsii.get(self, "customerManagedPolicyReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArnInput")
    def managed_policy_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedPolicyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArn")
    def managed_policy_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedPolicyArn"))

    @managed_policy_arn.setter
    def managed_policy_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b6770ead21b533414761074ee61623981c815184f9788c31d66412365bb89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary]:
        return typing.cast(typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f857dba5a0f48462c8ab0cfe4b179fc8e29919a5f535fdb74cacb120727eb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class SsoadminPermissionsBoundaryAttachmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#create SsoadminPermissionsBoundaryAttachment#create}.
        :param delete: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#delete SsoadminPermissionsBoundaryAttachment#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d894add550900dacf336ff10dba584d471b8a5c91d614ab42d0a2b3298ddb5)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#create SsoadminPermissionsBoundaryAttachment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/ssoadmin_permissions_boundary_attachment#delete SsoadminPermissionsBoundaryAttachment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SsoadminPermissionsBoundaryAttachmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SsoadminPermissionsBoundaryAttachmentTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.ssoadminPermissionsBoundaryAttachment.SsoadminPermissionsBoundaryAttachmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b0f7ffa1592333c337aaedf458d3a51385988bbb2b36a5d76eaa99405dbfc17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd754155c09e5ced3001919e643d6e8e51a5bbfb98d5ac596cef1a351ae51a2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9d040486d4b5cd8fade897a10b4b1ab6d12e1179343383e4cfe7d104ef961a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SsoadminPermissionsBoundaryAttachmentTimeouts]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SsoadminPermissionsBoundaryAttachmentTimeouts]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SsoadminPermissionsBoundaryAttachmentTimeouts]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf31fbbc23316051231e9dcb9b231d45d7d2ff783a7cf4a5ff00eaafd3d1e04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "SsoadminPermissionsBoundaryAttachment",
    "SsoadminPermissionsBoundaryAttachmentConfig",
    "SsoadminPermissionsBoundaryAttachmentPermissionsBoundary",
    "SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference",
    "SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReferenceOutputReference",
    "SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryOutputReference",
    "SsoadminPermissionsBoundaryAttachmentTimeouts",
    "SsoadminPermissionsBoundaryAttachmentTimeoutsOutputReference",
]

publication.publish()

def _typecheckingstub__aac360cbd595af5e5d17df342c3b75f2af1ea72f0cd85212cfd58319df8dee3c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_arn: builtins.str,
    permissions_boundary: typing.Union[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary, typing.Dict[builtins.str, typing.Any]],
    permission_set_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SsoadminPermissionsBoundaryAttachmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__646965b641b39312d4eb2b6657f2360563c60152ee6ebee75fa785137adf482a(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfd0f298accca344aab081ecc144c9367d15a0af586d631ca1009f792cf9325e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d26171e06c7058891aff3b2d9c935d91ad1d4f292bce62bd871662176a44f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e518989dbe576baaa9f2f96fe0a8697ab09a1947ca776fb1cb2584541f5103c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca0d766a63e1d730571d412526a5be94ca8ba42a57ee63d90ddfdc59bbd9fb2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_arn: builtins.str,
    permissions_boundary: typing.Union[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary, typing.Dict[builtins.str, typing.Any]],
    permission_set_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
    timeouts: typing.Optional[typing.Union[SsoadminPermissionsBoundaryAttachmentTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f158c814e3852c3a83bf5e200f730a4b2d1996f8d8c3b35e758ce06e0e3b92c5(
    *,
    customer_managed_policy_reference: typing.Optional[typing.Union[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference, typing.Dict[builtins.str, typing.Any]]] = None,
    managed_policy_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__526b8ca0830dcad2eb969465fb9c00d6d30e6ee5a88170e7e328c755e01195ea(
    *,
    name: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3934d77e7876e2173861436ce821725a0c8eb18bbf7166d6667997a5fb941a0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000f8afbb24d65e2b7af5aa65faa39ef7b74d219afbd1b641b2ac448f4bd58da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451692c76bce0eb5ae2068a4765c79bb68715906ef480693b0dd0027033afd0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803ffb4f90892f3c9cc4b36d72453240add7316c6bdee4e0d7a1860dde913648(
    value: typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundaryCustomerManagedPolicyReference],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__418768da61581982c6c71f530fcc5a10be0b273465e22057211812970289a23e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b6770ead21b533414761074ee61623981c815184f9788c31d66412365bb89c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f857dba5a0f48462c8ab0cfe4b179fc8e29919a5f535fdb74cacb120727eb2(
    value: typing.Optional[SsoadminPermissionsBoundaryAttachmentPermissionsBoundary],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d894add550900dacf336ff10dba584d471b8a5c91d614ab42d0a2b3298ddb5(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0f7ffa1592333c337aaedf458d3a51385988bbb2b36a5d76eaa99405dbfc17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd754155c09e5ced3001919e643d6e8e51a5bbfb98d5ac596cef1a351ae51a2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9d040486d4b5cd8fade897a10b4b1ab6d12e1179343383e4cfe7d104ef961a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf31fbbc23316051231e9dcb9b231d45d7d2ff783a7cf4a5ff00eaafd3d1e04(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SsoadminPermissionsBoundaryAttachmentTimeouts]],
) -> None:
    """Type checking stubs"""
    pass
