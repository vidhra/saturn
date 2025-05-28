# gcloud firebase test network-profiles  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles)*

**NAME**

: **gcloud firebase test network-profiles - explore network profiles available for testing**

**SYNOPSIS**

: **`gcloud firebase test network-profiles` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A network traffic profile consists of a set of parameters to emulate network
conditions when running a test. This feature only works on physical devices. The
network shaping parameters are:

- `RULE`: Where to apply traffic shaping. The UP rule shapes the
connection from the device to the internet. The DOWN rule shapes the connection
from the internet to the device.
- `DELAY`: The delay in packet transmission, in ms.
- `LOSS_RATIO`: The ratio of packets dropped during transmission.
- `DUPLICATION_RATIO`: The ratio of packets duplicated during
transmission.
- `BANDWIDTH`: The average packet transmission rate in kbits/s, as
defined by the token bucket algorithm.
- `BURST`: The total size, in kbits, by which packets can exceed the
bandwidth, as defined by the token bucket algorithm.

**EXAMPLES**

: To list all network profiles which can be used for testing, run:

```
gcloud firebase test network-profiles list
```

To view information about a specific network profile, run:

```
gcloud firebase test network-profiles describe PROFILE_ID
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[describe](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/describe)`**:
Describe a network profile.

**`[list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/list)`**:
List all network profiles available for testing.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test network-profiles
```

```
gcloud beta firebase test network-profiles
```