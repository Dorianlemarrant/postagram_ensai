r'''
# `aws_s3_bucket_logging`

Refer to the Terraform Registry for docs: [`aws_s3_bucket_logging`](https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging).
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


class S3BucketLoggingA(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingA",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging aws_s3_bucket_logging}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        bucket: builtins.str,
        target_bucket: builtins.str,
        target_prefix: builtins.str,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        target_grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLoggingTargetGrant", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_object_key_format: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormat", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging aws_s3_bucket_logging} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#bucket S3BucketLoggingA#bucket}.
        :param target_bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_bucket S3BucketLoggingA#target_bucket}.
        :param target_prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_prefix S3BucketLoggingA#target_prefix}.
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#expected_bucket_owner S3BucketLoggingA#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param target_grant: target_grant block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_grant S3BucketLoggingA#target_grant}
        :param target_object_key_format: target_object_key_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_object_key_format S3BucketLoggingA#target_object_key_format}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767c446a7d1309e18571aafac990b23e3b7d87068028dde241b3e731fb4f293a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3BucketLoggingAConfig(
            bucket=bucket,
            target_bucket=target_bucket,
            target_prefix=target_prefix,
            expected_bucket_owner=expected_bucket_owner,
            id=id,
            target_grant=target_grant,
            target_object_key_format=target_object_key_format,
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
        '''Generates CDKTF code for importing a S3BucketLoggingA resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the S3BucketLoggingA to import.
        :param import_from_id: The id of the existing S3BucketLoggingA that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the S3BucketLoggingA to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c9cccf569fdd87fb3643b629eb6e0d5ed062c4b9ffb8ce1548c0e342a4c5b34)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putTargetGrant")
    def put_target_grant(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLoggingTargetGrant", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9cfcc43f7798f9d8a94984b9e51418cb923980ebca5c48f2159e120b65e504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGrant", [value]))

    @jsii.member(jsii_name="putTargetObjectKeyFormat")
    def put_target_object_key_format(
        self,
        *,
        partitioned_prefix: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        simple_prefix: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormatSimplePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param partitioned_prefix: partitioned_prefix block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partitioned_prefix S3BucketLoggingA#partitioned_prefix}
        :param simple_prefix: simple_prefix block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#simple_prefix S3BucketLoggingA#simple_prefix}
        '''
        value = S3BucketLoggingTargetObjectKeyFormat(
            partitioned_prefix=partitioned_prefix, simple_prefix=simple_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putTargetObjectKeyFormat", [value]))

    @jsii.member(jsii_name="resetExpectedBucketOwner")
    def reset_expected_bucket_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpectedBucketOwner", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTargetGrant")
    def reset_target_grant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGrant", []))

    @jsii.member(jsii_name="resetTargetObjectKeyFormat")
    def reset_target_object_key_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetObjectKeyFormat", []))

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
    @jsii.member(jsii_name="targetGrant")
    def target_grant(self) -> "S3BucketLoggingTargetGrantList":
        return typing.cast("S3BucketLoggingTargetGrantList", jsii.get(self, "targetGrant"))

    @builtins.property
    @jsii.member(jsii_name="targetObjectKeyFormat")
    def target_object_key_format(
        self,
    ) -> "S3BucketLoggingTargetObjectKeyFormatOutputReference":
        return typing.cast("S3BucketLoggingTargetObjectKeyFormatOutputReference", jsii.get(self, "targetObjectKeyFormat"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwnerInput")
    def expected_bucket_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectedBucketOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="targetBucketInput")
    def target_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGrantInput")
    def target_grant_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLoggingTargetGrant"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLoggingTargetGrant"]]], jsii.get(self, "targetGrantInput"))

    @builtins.property
    @jsii.member(jsii_name="targetObjectKeyFormatInput")
    def target_object_key_format_input(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormat"]:
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormat"], jsii.get(self, "targetObjectKeyFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPrefixInput")
    def target_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a573a4b9557a17fe37f949f72bfeb174db855a79ac778462399ba66d9b5c9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expectedBucketOwner")
    def expected_bucket_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expectedBucketOwner"))

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef7d68e1396714e5bfcf8e9408a0bc1caaaf0599769b39ca424ef7ea679a93e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expectedBucketOwner", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__befcfdae931606b3cff4147c3151a66e1f786a18fb91ce936746248840ba32ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetBucket")
    def target_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetBucket"))

    @target_bucket.setter
    def target_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658180f1457e1e66f61804dc1b2e534b409bc63303abb631fd05d544db9fd0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetBucket", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetPrefix")
    def target_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPrefix"))

    @target_prefix.setter
    def target_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc335297478403a020e094e7814c37ebb9da5320316ba153f51bb61e420c42b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPrefix", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingAConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "bucket": "bucket",
        "target_bucket": "targetBucket",
        "target_prefix": "targetPrefix",
        "expected_bucket_owner": "expectedBucketOwner",
        "id": "id",
        "target_grant": "targetGrant",
        "target_object_key_format": "targetObjectKeyFormat",
    },
)
class S3BucketLoggingAConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        bucket: builtins.str,
        target_bucket: builtins.str,
        target_prefix: builtins.str,
        expected_bucket_owner: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        target_grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3BucketLoggingTargetGrant", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target_object_key_format: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormat", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#bucket S3BucketLoggingA#bucket}.
        :param target_bucket: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_bucket S3BucketLoggingA#target_bucket}.
        :param target_prefix: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_prefix S3BucketLoggingA#target_prefix}.
        :param expected_bucket_owner: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#expected_bucket_owner S3BucketLoggingA#expected_bucket_owner}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param target_grant: target_grant block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_grant S3BucketLoggingA#target_grant}
        :param target_object_key_format: target_object_key_format block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_object_key_format S3BucketLoggingA#target_object_key_format}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(target_object_key_format, dict):
            target_object_key_format = S3BucketLoggingTargetObjectKeyFormat(**target_object_key_format)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63433fe4275e9472bd333657f11d5d1d811262015c24979a188554ed90deb5dc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument target_bucket", value=target_bucket, expected_type=type_hints["target_bucket"])
            check_type(argname="argument target_prefix", value=target_prefix, expected_type=type_hints["target_prefix"])
            check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument target_grant", value=target_grant, expected_type=type_hints["target_grant"])
            check_type(argname="argument target_object_key_format", value=target_object_key_format, expected_type=type_hints["target_object_key_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
            "target_bucket": target_bucket,
            "target_prefix": target_prefix,
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
        if expected_bucket_owner is not None:
            self._values["expected_bucket_owner"] = expected_bucket_owner
        if id is not None:
            self._values["id"] = id
        if target_grant is not None:
            self._values["target_grant"] = target_grant
        if target_object_key_format is not None:
            self._values["target_object_key_format"] = target_object_key_format

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
    def bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#bucket S3BucketLoggingA#bucket}.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_bucket(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_bucket S3BucketLoggingA#target_bucket}.'''
        result = self._values.get("target_bucket")
        assert result is not None, "Required property 'target_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_prefix S3BucketLoggingA#target_prefix}.'''
        result = self._values.get("target_prefix")
        assert result is not None, "Required property 'target_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#expected_bucket_owner S3BucketLoggingA#expected_bucket_owner}.'''
        result = self._values.get("expected_bucket_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_grant(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLoggingTargetGrant"]]]:
        '''target_grant block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_grant S3BucketLoggingA#target_grant}
        '''
        result = self._values.get("target_grant")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3BucketLoggingTargetGrant"]]], result)

    @builtins.property
    def target_object_key_format(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormat"]:
        '''target_object_key_format block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#target_object_key_format S3BucketLoggingA#target_object_key_format}
        '''
        result = self._values.get("target_object_key_format")
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormat"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetGrant",
    jsii_struct_bases=[],
    name_mapping={"grantee": "grantee", "permission": "permission"},
)
class S3BucketLoggingTargetGrant:
    def __init__(
        self,
        *,
        grantee: typing.Union["S3BucketLoggingTargetGrantGrantee", typing.Dict[builtins.str, typing.Any]],
        permission: builtins.str,
    ) -> None:
        '''
        :param grantee: grantee block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#grantee S3BucketLoggingA#grantee}
        :param permission: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#permission S3BucketLoggingA#permission}.
        '''
        if isinstance(grantee, dict):
            grantee = S3BucketLoggingTargetGrantGrantee(**grantee)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ee3f58359db313296675d0e6c7203309a68b25237feec2ddac43b4486e23de)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "grantee": grantee,
            "permission": permission,
        }

    @builtins.property
    def grantee(self) -> "S3BucketLoggingTargetGrantGrantee":
        '''grantee block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#grantee S3BucketLoggingA#grantee}
        '''
        result = self._values.get("grantee")
        assert result is not None, "Required property 'grantee' is missing"
        return typing.cast("S3BucketLoggingTargetGrantGrantee", result)

    @builtins.property
    def permission(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#permission S3BucketLoggingA#permission}.'''
        result = self._values.get("permission")
        assert result is not None, "Required property 'permission' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingTargetGrant(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetGrantGrantee",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "email_address": "emailAddress",
        "id": "id",
        "uri": "uri",
    },
)
class S3BucketLoggingTargetGrantGrantee:
    def __init__(
        self,
        *,
        type: builtins.str,
        email_address: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#type S3BucketLoggingA#type}.
        :param email_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#email_address S3BucketLoggingA#email_address}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#uri S3BucketLoggingA#uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4042e47dbf009a922f612e874485352ec6301949ba27e100fac6267ef1353a7a)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if email_address is not None:
            self._values["email_address"] = email_address
        if id is not None:
            self._values["id"] = id
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#type S3BucketLoggingA#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#email_address S3BucketLoggingA#email_address}.'''
        result = self._values.get("email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#uri S3BucketLoggingA#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingTargetGrantGrantee(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLoggingTargetGrantGranteeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetGrantGranteeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee7db6b74092af0779b16992f523dfbdd6949a5b5662ffcede57d2cfef19a050)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmailAddress")
    def reset_email_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailAddress", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="emailAddressInput")
    def email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f87f4321e4206fab3570d81e050d4f7020338b9dfe7879283bb5b61a4400f82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c8ace187a46dace66e59b5d25525a8e412c96a686994578993b0a3e36986e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0265f0e454c3f34b7dfbe2e600031b1453097664ac5230a435588b8ba439e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__184dc4e840b6fbfca7aa95463a5a59d6fe3e1d0c3ded50cfb971245914939607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketLoggingTargetGrantGrantee]:
        return typing.cast(typing.Optional[S3BucketLoggingTargetGrantGrantee], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLoggingTargetGrantGrantee],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f248aeccf4298392b8128c3e3f59b22ce2d7233294f859d83a10079ead4d445c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class S3BucketLoggingTargetGrantList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetGrantList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff6139c3ef410d954479746518a94c0becab2bbc15df70adf258418f21f8a211)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "S3BucketLoggingTargetGrantOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44969abd9508fb51af111f542545325ef02883eebec70c097126b9f14d2a0fe6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3BucketLoggingTargetGrantOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b38deeae4f977498400a1b0e24e36254d2cb79c4617779cb12f0a4b8ef9019a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__257716bd6a7ee3b911b9a5a924fde8ec1314264c962bbb15e1f26c79d3be3d40)
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
            type_hints = typing.get_type_hints(_typecheckingstub__778938ce7040f61d22ef13bb3364293a7c03bf0728ee2afb92825c10010feb80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLoggingTargetGrant]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLoggingTargetGrant]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLoggingTargetGrant]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05cbe2ff1ead87c634cc0462b5a446a40bfc69b38df5657b902a5d029f9cf54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class S3BucketLoggingTargetGrantOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetGrantOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9579b6fd9669b0143c8222e412cc4deef52e027bce237d195ed8722df737ce71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putGrantee")
    def put_grantee(
        self,
        *,
        type: builtins.str,
        email_address: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#type S3BucketLoggingA#type}.
        :param email_address: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#email_address S3BucketLoggingA#email_address}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#id S3BucketLoggingA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#uri S3BucketLoggingA#uri}.
        '''
        value = S3BucketLoggingTargetGrantGrantee(
            type=type, email_address=email_address, id=id, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putGrantee", [value]))

    @builtins.property
    @jsii.member(jsii_name="grantee")
    def grantee(self) -> S3BucketLoggingTargetGrantGranteeOutputReference:
        return typing.cast(S3BucketLoggingTargetGrantGranteeOutputReference, jsii.get(self, "grantee"))

    @builtins.property
    @jsii.member(jsii_name="granteeInput")
    def grantee_input(self) -> typing.Optional[S3BucketLoggingTargetGrantGrantee]:
        return typing.cast(typing.Optional[S3BucketLoggingTargetGrantGrantee], jsii.get(self, "granteeInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f83c8b5fa0e9d4b10bfae3aed50ff0457af2c9c031d9646ec07aa18ae77b8e46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, S3BucketLoggingTargetGrant]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, S3BucketLoggingTargetGrant]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, S3BucketLoggingTargetGrant]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a961426fe83e2245d05624a54e966378b23f7f91787588e3936c7bbfe3622fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormat",
    jsii_struct_bases=[],
    name_mapping={
        "partitioned_prefix": "partitionedPrefix",
        "simple_prefix": "simplePrefix",
    },
)
class S3BucketLoggingTargetObjectKeyFormat:
    def __init__(
        self,
        *,
        partitioned_prefix: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix", typing.Dict[builtins.str, typing.Any]]] = None,
        simple_prefix: typing.Optional[typing.Union["S3BucketLoggingTargetObjectKeyFormatSimplePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param partitioned_prefix: partitioned_prefix block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partitioned_prefix S3BucketLoggingA#partitioned_prefix}
        :param simple_prefix: simple_prefix block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#simple_prefix S3BucketLoggingA#simple_prefix}
        '''
        if isinstance(partitioned_prefix, dict):
            partitioned_prefix = S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix(**partitioned_prefix)
        if isinstance(simple_prefix, dict):
            simple_prefix = S3BucketLoggingTargetObjectKeyFormatSimplePrefix(**simple_prefix)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed554d8e3a7a8994f22c856a53d2aa488e19681615b17e873aa7c9f93739d115)
            check_type(argname="argument partitioned_prefix", value=partitioned_prefix, expected_type=type_hints["partitioned_prefix"])
            check_type(argname="argument simple_prefix", value=simple_prefix, expected_type=type_hints["simple_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if partitioned_prefix is not None:
            self._values["partitioned_prefix"] = partitioned_prefix
        if simple_prefix is not None:
            self._values["simple_prefix"] = simple_prefix

    @builtins.property
    def partitioned_prefix(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix"]:
        '''partitioned_prefix block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partitioned_prefix S3BucketLoggingA#partitioned_prefix}
        '''
        result = self._values.get("partitioned_prefix")
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix"], result)

    @builtins.property
    def simple_prefix(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormatSimplePrefix"]:
        '''simple_prefix block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#simple_prefix S3BucketLoggingA#simple_prefix}
        '''
        result = self._values.get("simple_prefix")
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormatSimplePrefix"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingTargetObjectKeyFormat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLoggingTargetObjectKeyFormatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d063240e3ff4289b6d3fde576481313413fb61eadb62528322809f6ae6c024c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPartitionedPrefix")
    def put_partitioned_prefix(self, *, partition_date_source: builtins.str) -> None:
        '''
        :param partition_date_source: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partition_date_source S3BucketLoggingA#partition_date_source}.
        '''
        value = S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix(
            partition_date_source=partition_date_source
        )

        return typing.cast(None, jsii.invoke(self, "putPartitionedPrefix", [value]))

    @jsii.member(jsii_name="putSimplePrefix")
    def put_simple_prefix(self) -> None:
        value = S3BucketLoggingTargetObjectKeyFormatSimplePrefix()

        return typing.cast(None, jsii.invoke(self, "putSimplePrefix", [value]))

    @jsii.member(jsii_name="resetPartitionedPrefix")
    def reset_partitioned_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionedPrefix", []))

    @jsii.member(jsii_name="resetSimplePrefix")
    def reset_simple_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimplePrefix", []))

    @builtins.property
    @jsii.member(jsii_name="partitionedPrefix")
    def partitioned_prefix(
        self,
    ) -> "S3BucketLoggingTargetObjectKeyFormatPartitionedPrefixOutputReference":
        return typing.cast("S3BucketLoggingTargetObjectKeyFormatPartitionedPrefixOutputReference", jsii.get(self, "partitionedPrefix"))

    @builtins.property
    @jsii.member(jsii_name="simplePrefix")
    def simple_prefix(
        self,
    ) -> "S3BucketLoggingTargetObjectKeyFormatSimplePrefixOutputReference":
        return typing.cast("S3BucketLoggingTargetObjectKeyFormatSimplePrefixOutputReference", jsii.get(self, "simplePrefix"))

    @builtins.property
    @jsii.member(jsii_name="partitionedPrefixInput")
    def partitioned_prefix_input(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix"]:
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix"], jsii.get(self, "partitionedPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="simplePrefixInput")
    def simple_prefix_input(
        self,
    ) -> typing.Optional["S3BucketLoggingTargetObjectKeyFormatSimplePrefix"]:
        return typing.cast(typing.Optional["S3BucketLoggingTargetObjectKeyFormatSimplePrefix"], jsii.get(self, "simplePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[S3BucketLoggingTargetObjectKeyFormat]:
        return typing.cast(typing.Optional[S3BucketLoggingTargetObjectKeyFormat], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLoggingTargetObjectKeyFormat],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5a142f249ad618540cc185cb196607c35518fa76574284b51e153c0b98dcfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix",
    jsii_struct_bases=[],
    name_mapping={"partition_date_source": "partitionDateSource"},
)
class S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix:
    def __init__(self, *, partition_date_source: builtins.str) -> None:
        '''
        :param partition_date_source: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partition_date_source S3BucketLoggingA#partition_date_source}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bea644a064a5c28c3dcee2e6d2af1d93e7a33d692b6f88487875458c567e174)
            check_type(argname="argument partition_date_source", value=partition_date_source, expected_type=type_hints["partition_date_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partition_date_source": partition_date_source,
        }

    @builtins.property
    def partition_date_source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.97.0/docs/resources/s3_bucket_logging#partition_date_source S3BucketLoggingA#partition_date_source}.'''
        result = self._values.get("partition_date_source")
        assert result is not None, "Required property 'partition_date_source' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLoggingTargetObjectKeyFormatPartitionedPrefixOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormatPartitionedPrefixOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4f35dc635cfcbb4a325d94f4b797770526c1e015d2c6080b7d8ecf7e3ecf32e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="partitionDateSourceInput")
    def partition_date_source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionDateSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionDateSource")
    def partition_date_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionDateSource"))

    @partition_date_source.setter
    def partition_date_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__227449f8f393fc1f91edf029216c7146f454dfd91826d6a5d1dacd4249393f92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionDateSource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix]:
        return typing.cast(typing.Optional[S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b979f128fe749633b6d81f1afdda8984d885290af6acf206c70b547544f700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormatSimplePrefix",
    jsii_struct_bases=[],
    name_mapping={},
)
class S3BucketLoggingTargetObjectKeyFormatSimplePrefix:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketLoggingTargetObjectKeyFormatSimplePrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketLoggingTargetObjectKeyFormatSimplePrefixOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3BucketLogging.S3BucketLoggingTargetObjectKeyFormatSimplePrefixOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__928c1ff2b7546d8806c5bd210ddb95ecc7b3ffeb1169c4be858d1d36b4c87929)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3BucketLoggingTargetObjectKeyFormatSimplePrefix]:
        return typing.cast(typing.Optional[S3BucketLoggingTargetObjectKeyFormatSimplePrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3BucketLoggingTargetObjectKeyFormatSimplePrefix],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225eac65341f262d35d1d3307de03daaeecc473e1a6ec0a694933dd3dfd542da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "S3BucketLoggingA",
    "S3BucketLoggingAConfig",
    "S3BucketLoggingTargetGrant",
    "S3BucketLoggingTargetGrantGrantee",
    "S3BucketLoggingTargetGrantGranteeOutputReference",
    "S3BucketLoggingTargetGrantList",
    "S3BucketLoggingTargetGrantOutputReference",
    "S3BucketLoggingTargetObjectKeyFormat",
    "S3BucketLoggingTargetObjectKeyFormatOutputReference",
    "S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix",
    "S3BucketLoggingTargetObjectKeyFormatPartitionedPrefixOutputReference",
    "S3BucketLoggingTargetObjectKeyFormatSimplePrefix",
    "S3BucketLoggingTargetObjectKeyFormatSimplePrefixOutputReference",
]

publication.publish()

def _typecheckingstub__767c446a7d1309e18571aafac990b23e3b7d87068028dde241b3e731fb4f293a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    bucket: builtins.str,
    target_bucket: builtins.str,
    target_prefix: builtins.str,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    target_grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLoggingTargetGrant, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_object_key_format: typing.Optional[typing.Union[S3BucketLoggingTargetObjectKeyFormat, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__6c9cccf569fdd87fb3643b629eb6e0d5ed062c4b9ffb8ce1548c0e342a4c5b34(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9cfcc43f7798f9d8a94984b9e51418cb923980ebca5c48f2159e120b65e504(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLoggingTargetGrant, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a573a4b9557a17fe37f949f72bfeb174db855a79ac778462399ba66d9b5c9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7d68e1396714e5bfcf8e9408a0bc1caaaf0599769b39ca424ef7ea679a93e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__befcfdae931606b3cff4147c3151a66e1f786a18fb91ce936746248840ba32ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658180f1457e1e66f61804dc1b2e534b409bc63303abb631fd05d544db9fd0f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc335297478403a020e094e7814c37ebb9da5320316ba153f51bb61e420c42b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63433fe4275e9472bd333657f11d5d1d811262015c24979a188554ed90deb5dc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    bucket: builtins.str,
    target_bucket: builtins.str,
    target_prefix: builtins.str,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    target_grant: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3BucketLoggingTargetGrant, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target_object_key_format: typing.Optional[typing.Union[S3BucketLoggingTargetObjectKeyFormat, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ee3f58359db313296675d0e6c7203309a68b25237feec2ddac43b4486e23de(
    *,
    grantee: typing.Union[S3BucketLoggingTargetGrantGrantee, typing.Dict[builtins.str, typing.Any]],
    permission: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4042e47dbf009a922f612e874485352ec6301949ba27e100fac6267ef1353a7a(
    *,
    type: builtins.str,
    email_address: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7db6b74092af0779b16992f523dfbdd6949a5b5662ffcede57d2cfef19a050(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f87f4321e4206fab3570d81e050d4f7020338b9dfe7879283bb5b61a4400f82d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c8ace187a46dace66e59b5d25525a8e412c96a686994578993b0a3e36986e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0265f0e454c3f34b7dfbe2e600031b1453097664ac5230a435588b8ba439e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__184dc4e840b6fbfca7aa95463a5a59d6fe3e1d0c3ded50cfb971245914939607(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f248aeccf4298392b8128c3e3f59b22ce2d7233294f859d83a10079ead4d445c(
    value: typing.Optional[S3BucketLoggingTargetGrantGrantee],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6139c3ef410d954479746518a94c0becab2bbc15df70adf258418f21f8a211(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44969abd9508fb51af111f542545325ef02883eebec70c097126b9f14d2a0fe6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b38deeae4f977498400a1b0e24e36254d2cb79c4617779cb12f0a4b8ef9019a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257716bd6a7ee3b911b9a5a924fde8ec1314264c962bbb15e1f26c79d3be3d40(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__778938ce7040f61d22ef13bb3364293a7c03bf0728ee2afb92825c10010feb80(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f05cbe2ff1ead87c634cc0462b5a446a40bfc69b38df5657b902a5d029f9cf54(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3BucketLoggingTargetGrant]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9579b6fd9669b0143c8222e412cc4deef52e027bce237d195ed8722df737ce71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f83c8b5fa0e9d4b10bfae3aed50ff0457af2c9c031d9646ec07aa18ae77b8e46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a961426fe83e2245d05624a54e966378b23f7f91787588e3936c7bbfe3622fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, S3BucketLoggingTargetGrant]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed554d8e3a7a8994f22c856a53d2aa488e19681615b17e873aa7c9f93739d115(
    *,
    partitioned_prefix: typing.Optional[typing.Union[S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix, typing.Dict[builtins.str, typing.Any]]] = None,
    simple_prefix: typing.Optional[typing.Union[S3BucketLoggingTargetObjectKeyFormatSimplePrefix, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d063240e3ff4289b6d3fde576481313413fb61eadb62528322809f6ae6c024c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5a142f249ad618540cc185cb196607c35518fa76574284b51e153c0b98dcfe(
    value: typing.Optional[S3BucketLoggingTargetObjectKeyFormat],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bea644a064a5c28c3dcee2e6d2af1d93e7a33d692b6f88487875458c567e174(
    *,
    partition_date_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f35dc635cfcbb4a325d94f4b797770526c1e015d2c6080b7d8ecf7e3ecf32e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227449f8f393fc1f91edf029216c7146f454dfd91826d6a5d1dacd4249393f92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b979f128fe749633b6d81f1afdda8984d885290af6acf206c70b547544f700(
    value: typing.Optional[S3BucketLoggingTargetObjectKeyFormatPartitionedPrefix],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928c1ff2b7546d8806c5bd210ddb95ecc7b3ffeb1169c4be858d1d36b4c87929(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225eac65341f262d35d1d3307de03daaeecc473e1a6ec0a694933dd3dfd542da(
    value: typing.Optional[S3BucketLoggingTargetObjectKeyFormatSimplePrefix],
) -> None:
    """Type checking stubs"""
    pass
