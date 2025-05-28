# gcloud artifacts repositories create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create)*

**NAME**

: **gcloud artifacts repositories create - create an Artifact Registry repository**

**SYNOPSIS**

: **`gcloud artifacts repositories create` (`[REPOSITORY](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#REPOSITORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--location)`=`LOCATION`) `[--repository-format](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--repository-format)`=`REPOSITORY_FORMAT` [`[--allow-snapshot-overwrites](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--allow-snapshot-overwrites)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--description)`=`DESCRIPTION`] [`[--disable-remote-validation](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--disable-remote-validation)`] [`[--immutable-tags](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--immutable-tags)`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--kms-key)`=`KMS_KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--mode)`=`MODE`; default="NONE"] [`[--remote-apt-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-apt-repo)`=`REMOTE_APT_REPO`] [`[--remote-apt-repo-path](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-apt-repo-path)`=`REMOTE_APT_REPO_PATH`] [`[--remote-docker-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-docker-repo)`=`REMOTE_DOCKER_REPO`] [`[--remote-go-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-go-repo)`=`REMOTE_GO_REPO`] [`[--remote-mvn-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-mvn-repo)`=`REMOTE_MVN_REPO`] [`[--remote-npm-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-npm-repo)`=`REMOTE_NPM_REPO`] [`[--remote-password-secret-version](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-password-secret-version)`=`REMOTE_PASSWORD_SECRET_VERSION`] [`[--remote-python-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-python-repo)`=`REMOTE_PYTHON_REPO`] [`[--remote-repo-config-desc](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-repo-config-desc)`=`REMOTE_REPO_CONFIG_DESC`] [`[--remote-username](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-username)`=`REMOTE_USERNAME`] [`[--remote-yum-repo](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-yum-repo)`=`REMOTE_YUM_REPO`] [`[--remote-yum-repo-path](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--remote-yum-repo-path)`=`REMOTE_YUM_REPO_PATH`] [`[--upstream-policy-file](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--upstream-policy-file)`=`FILE`] [`[--version-policy](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--version-policy)`=`VERSION_POLICY`] [`[--allow-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--allow-vulnerability-scanning)`     | `[--disable-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#--disable-vulnerability-scanning)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Artifact Registry repository.
This command can fail for the following reasons:

- A repository with the same name already exists.
- The active account does not have permission to create repositories.
- A valid repository format was not provided.

**EXAMPLES**

: To create a docker repository with the name `my-repo` in the default
project and location, run the following command:

```
gcloud artifacts repositories create my-repo --repository-format=docker
```

To create a docker repository `my-repo` with a KMS key
`projects/my-project/locations/us/keyRings/my-kr/cryptoKeys/my-key`
in the default project and location, run the following command:

```
gcloud artifacts repositories create my-repo --repository-format=docker --kms-key=projects/my-project/locations/us/keyRings/my-kr/cryptoKeys/my-key
```

**POSITIONAL ARGUMENTS**

: **Repository resource - The Artifact Registry repository to create. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`REPOSITORY`**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `repository` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the repository. Overrides the default artifacts/location property
value for this command invocation. To configure the default location, use the
command: gcloud config set artifacts/location.
To set the `location` attribute:

- provide the argument `repository` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.**

**REQUIRED FLAGS**

: **--repository-format**:
Format of the repository. REPOSITORY_FORMAT must be one of:

```
apt
   APT package format.
docker
   Docker image format.
go
   Go module format.
kfp
   KFP package format.
maven
   Maven package format.
npm
   NPM package format.
python
   Python package format.
yum
   YUM package format.
```

**OPTIONAL FLAGS**

: **--allow-snapshot-overwrites**:
(Maven only) Allow repository users to publish a snapshot that overwrites the
same snapshot version in the repository.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description for the repository.

**--disable-remote-validation**:
Do not make an HTTP request to validate the remote upstream. Not recommended
when setting a custom remote upstream unless you are absolutely sure your
upstream URI and any auth is valid.

**--immutable-tags**:
(Docker only) Prevent changes to tagged images in the repository. Tags cannot be
deleted or moved to a different image digest, and tagged images cannot be
deleted.

**--kms-key**:
Name of the encryption key that's used for encrypting the contents of the
repository.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--mode**:
Mode is the type of the repository - Standard, Virtual or Remote.
`MODE` must be one of:

**`none`**:
Repository mode not specified.

**`remote-repository`**:
Remote repository mode - fetches data from upstream and caches it.

**`standard-repository`**:
Standard repository mode - should be possible to write/read data to this repo.

**`virtual-repository`**:
Virtual repository mode - aggregates data from several upstreams.

**--remote-apt-repo**:
(Apt only) Repository base for apt remote repository. REMOTE_APT_REPO must be
one of: [debian, debian-snapshot, ubuntu].

**--remote-apt-repo-path**:
(Apt only) Remaining URL path to apt remote repository.

**--remote-docker-repo**:
(Docker only) Repo upstream for docker remote repository. REMOTE_DOCKER_REPO can
be either:

- one of the following enums: [docker-hub].
- an http/https custom registry uri (ex: https://my.docker.registry)

**--remote-go-repo**:
(Go only) Repo upstream for Go remote repository. "https://proxy.golang.org/" is
the only valid value.

**--remote-mvn-repo**:
(Maven only) Repo upstream for maven remote repository. REMOTE_MVN_REPO can be
either:

- one of the following enums: [maven-central].
- an http/https custom registry uri (ex: https://my.maven.registry)

**--remote-npm-repo**:
(Npm only) Repo upstream for npm remote repository. REMOTE_NPM_REPO can be
either:

- one of the following enums: [npmjs].
- an http/https custom registry uri (ex: https://my.npm.registry)

**--remote-password-secret-version**:
Secret Manager secret version that contains password for the remote repository
upstream.

**--remote-python-repo**:
(Python only) Repo upstream for python remote repository. REMOTE_PYTHON_REPO can
be either:

- one of the following enums: [pypi].
- an http/https custom registry uri (ex: https://my.python.registry)

**--remote-repo-config-desc**:
The description for the remote repository config.

**--remote-username**:
Remote Repository upstream registry username.

**--remote-yum-repo**:
(Yum only) Repository base for yum remote repository. REMOTE_YUM_REPO must be
one of: [centos, centos-debug, centos-stream, centos-vault, epel, rocky].

**--remote-yum-repo-path**:
(Yum only) Remaining URL path to yum remote repository.

**--upstream-policy-file**:
(Virtual Repositories only) is the upstreams for the Virtual Repository. Example
of the file contents: [ { "id": "test1", "repository":
"projects/p1/locations/us-central1/repositories/repo1", "priority": 1 }, { "id":
"test2", "repository": "projects/p2/locations/us-west2/repositories/repo2",
"priority": 2 } ]

**--version-policy**:
(Maven only) The package versions that the repository will store.
`VERSION_POLICY` must be one of:

**`none`**:
(Maven only) The repository doesn't validate the version type.

**`release`**:
(Maven only) The repository accepts release versions only.

**`snapshot`**:
(Maven only) The repository accepts snapshot versions only.

**--allow-vulnerability-scanning**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts repositories create
```

```
gcloud beta artifacts repositories create
```