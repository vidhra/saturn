# gcloud compute  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute](https://cloud.google.com/sdk/gcloud/reference/compute)*

**NAME**

: **gcloud compute - create and manipulate Compute Engine resources**

**SYNOPSIS**

: **`gcloud compute` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud compute command group lets you create, configure, and manipulate
Compute Engine virtual machine (VM) instances.
With Compute Engine, you can create and run VMs on Google's infrastructure.
Compute Engine offers scale, performance, and value that lets you launch large
compute clusters on Google's infrastructure.
For more information about Compute Engine, see the [Compute Engine overview](https://cloud.google.com/compute/) and the [Compute Engine user
documentation](https://cloud.google.com/compute/docs/).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[accelerator-types](https://cloud.google.com/sdk/gcloud/reference/compute/accelerator-types)`**:
Read Compute Engine accelerator types.

**`[addresses](https://cloud.google.com/sdk/gcloud/reference/compute/addresses)`**:
Read and manipulate Compute Engine addresses.

**`[backend-buckets](https://cloud.google.com/sdk/gcloud/reference/compute/backend-buckets)`**:
Read and manipulate backend buckets.

**`[backend-services](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services)`**:
List, create, and delete backend services.

**`[commitments](https://cloud.google.com/sdk/gcloud/reference/compute/commitments)`**:
Manage Compute Engine commitments.

**`[diagnose](https://cloud.google.com/sdk/gcloud/reference/compute/diagnose)`**:
Debugging tools for Compute Engine virtual machine instances.

**`[disk-types](https://cloud.google.com/sdk/gcloud/reference/compute/disk-types)`**:
Read Compute Engine virtual disk types.

**`[disks](https://cloud.google.com/sdk/gcloud/reference/compute/disks)`**:
Read and manipulate Compute Engine disks.

**`[external-vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways)`**:
List, create, delete and update External VPN Gateways.

**`[firewall-policies](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-policies)`**:
Manage Compute Engine organization firewall policies.

**`[firewall-rules](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules)`**:
List, create, update, and delete Compute Engine firewall rules.

**`[forwarding-rules](https://cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules)`**:
Read and manipulate traffic forwarding rules to network load balancers.

**`[health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks)`**:
Read and manipulate health checks for load balanced instances.

**`[http-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/http-health-checks)`**:
Read and manipulate HTTP health checks for load balanced instances.

**`[https-health-checks](https://cloud.google.com/sdk/gcloud/reference/compute/https-health-checks)`**:
Read and manipulate HTTPS health checks for load balanced instances.

**`[images](https://cloud.google.com/sdk/gcloud/reference/compute/images)`**:
List, create, and delete Compute Engine images.

**`[instance-groups](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups)`**:
Read and manipulate Compute Engine instance groups.

**`[instance-templates](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates)`**:
Read and manipulate Compute Engine instances templates.

**`[instances](https://cloud.google.com/sdk/gcloud/reference/compute/instances)`**:
Read and manipulate Compute Engine virtual machine instances.

**`[instant-snapshots](https://cloud.google.com/sdk/gcloud/reference/compute/instant-snapshots)`**:
Create, list and delete Compute Engine instant snapshots.

**`[interconnects](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects)`**:
Read and manipulate Compute Engine interconnects.

**`[machine-images](https://cloud.google.com/sdk/gcloud/reference/compute/machine-images)`**:
Read and manage Compute Engine machine image resources.

**`[machine-types](https://cloud.google.com/sdk/gcloud/reference/compute/machine-types)`**:
Read Compute Engine virtual machine types.

**`[network-attachments](https://cloud.google.com/sdk/gcloud/reference/compute/network-attachments)`**:
Manage Compute Engine network attachment resources.

**`[network-edge-security-services](https://cloud.google.com/sdk/gcloud/reference/compute/network-edge-security-services)`**:
Read and manipulate network edge security services.

**`[network-endpoint-groups](https://cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups)`**:
Read and manipulate Compute Engine network endpoint groups.

**`[network-firewall-policies](https://cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies)`**:
Manage Compute Engine network firewall policies.

**`[network-profiles](https://cloud.google.com/sdk/gcloud/reference/compute/network-profiles)`**:
Read Compute Engine network profiles.

**`[networks](https://cloud.google.com/sdk/gcloud/reference/compute/networks)`**:
List, create, and delete Compute Engine networks.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/compute/operations)`**:
Read and manipulate Compute Engine operations.

**`[os-config](https://cloud.google.com/sdk/gcloud/reference/compute/os-config)`**:
Manage OS Config tasks for Compute Engine VM instances.

**`[os-login](https://cloud.google.com/sdk/gcloud/reference/compute/os-login)`**:
Create and manipulate Compute Engine OS Login resources.

**`[packet-mirrorings](https://cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings)`**:
Manage Compute Engine packet mirroring resources.

**`[project-info](https://cloud.google.com/sdk/gcloud/reference/compute/project-info)`**:
Read and manipulate project-level data like quotas and metadata.

**`[project-zonal-metadata](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata)`**:
Describe and update project zonal metadata.

**`[public-advertised-prefixes](https://cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes)`**:
Manage public advertised prefix resources.

**`[public-delegated-prefixes](https://cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes)`**:
Manage public delegated prefix resources.

**`[regions](https://cloud.google.com/sdk/gcloud/reference/compute/regions)`**:
List Compute Engine regions.

**`[reservations](https://cloud.google.com/sdk/gcloud/reference/compute/reservations)`**:
Manage Compute Engine reservations.

**`[resource-policies](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies)`**:
Manage Compute Engine Resource Policies.

**`[routers](https://cloud.google.com/sdk/gcloud/reference/compute/routers)`**:
List, create, and delete Compute Engine routers.

**`[routes](https://cloud.google.com/sdk/gcloud/reference/compute/routes)`**:
Read and manipulate routes.

**`[security-policies](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies)`**:
Read and manipulate Cloud Armor security policies.

**`[service-attachments](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments)`**:
Manage Compute Engine service attachment resources.

**`[shared-vpc](https://cloud.google.com/sdk/gcloud/reference/compute/shared-vpc)`**:
Configure shared VPC.

**`[snapshot-settings](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings)`**:
Describe and update Compute Engine snapshot settings.

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots)`**:
List, describe, and delete Compute Engine snapshots.

**`[sole-tenancy](https://cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy)`**:
Read and manage Compute Engine sole-tenancy resources.

**`[ssl-certificates](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates)`**:
List, create, and delete Compute Engine SSL certificate resources.

**`[ssl-policies](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-policies)`**:
List, create, delete and update Compute Engine SSL policies.

**`[storage-pool-types](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types)`**:
Read storage pool types.

**`[storage-pools](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools)`**:
Read and manipulate storage pools.

**`[target-grpc-proxies](https://cloud.google.com/sdk/gcloud/reference/compute/target-grpc-proxies)`**:
Manage Compute Engine target gRPC proxy resources.

**`[target-http-proxies](https://cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies)`**:
List, create, and delete target HTTP proxies.

**`[target-https-proxies](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies)`**:
List, create, and delete target HTTPS proxies.

**`[target-instances](https://cloud.google.com/sdk/gcloud/reference/compute/target-instances)`**:
Read and manipulate Compute Engine virtual target instances.

**`[target-pools](https://cloud.google.com/sdk/gcloud/reference/compute/target-pools)`**:
Control Compute Engine target pools for network load balancing.

**`[target-ssl-proxies](https://cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies)`**:
List, create, and delete target SSL proxies.

**`[target-tcp-proxies](https://cloud.google.com/sdk/gcloud/reference/compute/target-tcp-proxies)`**:
List, create, and delete target TCP proxies.

**`[target-vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways)`**:
Read and manipulate classic VPN gateways.

**`[tpus](https://cloud.google.com/sdk/gcloud/reference/compute/tpus)`**:
List, create, and delete Cloud TPUs.

**`[url-maps](https://cloud.google.com/sdk/gcloud/reference/compute/url-maps)`**:
List, create, and delete URL maps.

**`[vpn-gateways](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways)`**:
read and manipulate Highly Available VPN Gateways.

**`[vpn-tunnels](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels)`**:
Read and manipulate Compute Engine VPN tunnels.

**`[zones](https://cloud.google.com/sdk/gcloud/reference/compute/zones)`**:
List Compute Engine zones.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[config-ssh](https://cloud.google.com/sdk/gcloud/reference/compute/config-ssh)`**:
Populate SSH config files with Host entries from each instance.

**`[connect-to-serial-port](https://cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port)`**:
Connect to the serial port of an instance.

**`[copy-files](https://cloud.google.com/sdk/gcloud/reference/compute/copy-files)`**:
Copy files to and from Google Compute Engine virtual machines via scp.

**`[reset-windows-password](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password)`**:
Reset and return a password for a Windows machine instance.

**`[scp](https://cloud.google.com/sdk/gcloud/reference/compute/scp)`**:
Copy files to and from Google Compute Engine virtual machines via scp.

**`[sign-url](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url)`**:
Sign specified URL for use with Cloud CDN Signed URLs.

**`[ssh](https://cloud.google.com/sdk/gcloud/reference/compute/ssh)`**:
SSH into a virtual machine instance.

**`[start-iap-tunnel](https://cloud.google.com/sdk/gcloud/reference/compute/start-iap-tunnel)`**:
Starts an IAP TCP forwarding tunnel.

**NOTES**

: These variants are also available:

```
gcloud alpha compute
```

```
gcloud beta compute
```