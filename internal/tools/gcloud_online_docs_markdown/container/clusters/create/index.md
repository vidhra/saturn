# gcloud container clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)*

**NAME**

: **gcloud container clusters create - create a cluster for running containers**

**SYNOPSIS**

: **`gcloud container clusters create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#NAME)` [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`,`gpu-driver-version`=`GPU_DRIVER_VERSION`,`gpu-partition-size`=`GPU_PARTITION_SIZE`,`gpu-sharing-strategy`=`GPU_SHARING_STRATEGY`,`max-shared-clients-per-gpu`=`MAX_SHARED_CLIENTS_PER_GPU`],…]] [`[--additional-zones](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--additional-zones)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#ZONE)`,…]] [`[--addons](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--addons)`=[`ADDON`[=`ENABLED`|`[DISABLED](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#DISABLED)`],…]] [`[--anonymous-authentication-config](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--anonymous-authentication-config)`=`ANONYMOUS_AUTHENTICATION_CONFIG`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--async)`] [`[--auto-monitoring-scope](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--auto-monitoring-scope)`=`AUTO_MONITORING_SCOPE`] [`[--autoprovisioning-enable-insecure-kubelet-readonly-port](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-enable-insecure-kubelet-readonly-port)`] [`[--autoprovisioning-network-tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-network-tags)`=`TAGS`,[`[TAGS](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#TAGS)`,…]] [`[--autoprovisioning-resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--autoscaling-profile](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoscaling-profile)`=`AUTOSCALING_PROFILE`] [`[--boot-disk-kms-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--boot-disk-kms-key)`=`BOOT_DISK_KMS_KEY`] [`[--cloud-run-config](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cloud-run-config)`=[`load-balancer-type`=`EXTERNAL`,…]] [`[--cluster-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-ipv4-cidr)`=`CLUSTER_IPV4_CIDR`] [`[--cluster-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-secondary-range-name)`=`NAME`] [`[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-version)`=`CLUSTER_VERSION`] [`[--confidential-node-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--confidential-node-type)`=`CONFIDENTIAL_NODE_TYPE`] [`[--containerd-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--containerd-config-from-file)`=`PATH_TO_FILE`] [`[--create-subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--create-subnetwork)`=[`KEY`=`VALUE`,…]] [`[--data-cache-count](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--data-cache-count)`=`DATA_CACHE_COUNT`] [`[--database-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--database-encryption-key)`=`DATABASE_ENCRYPTION_KEY`] [`[--default-max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--default-max-pods-per-node)`=`DEFAULT_MAX_PODS_PER_NODE`] [`[--disable-default-snat](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-default-snat)`] [`[--disable-l4-lb-firewall-reconciliation](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-l4-lb-firewall-reconciliation)`] [`[--disk-size](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disk-size)`=`DISK_SIZE`] [`[--disk-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disk-type)`=`DISK_TYPE`] [`[--enable-authorized-networks-on-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-authorized-networks-on-private-endpoint)`] [`[--enable-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autorepair)`] [`[--no-enable-autoupgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoupgrade)`] [`[--enable-cilium-clusterwide-network-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cilium-clusterwide-network-policy)`] [`[--enable-cloud-logging](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cloud-logging)`] [`[--enable-cloud-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cloud-monitoring)`] [`[--enable-cloud-run-alpha](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cloud-run-alpha)`] [`[--enable-confidential-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-confidential-nodes)`] [`[--enable-confidential-storage](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-confidential-storage)`] [`[--enable-cost-allocation](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-cost-allocation)`] [`[--enable-dataplane-v2](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-dataplane-v2)`] [`[--enable-dns-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-dns-access)`] [`[--enable-fleet](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-fleet)`] [`[--enable-fqdn-network-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-fqdn-network-policy)`] [`[--enable-google-cloud-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-google-cloud-access)`] [`[--enable-gvnic](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-gvnic)`] [`[--enable-identity-service](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-identity-service)`] [`[--enable-image-streaming](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-image-streaming)`] [`[--enable-insecure-kubelet-readonly-port](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-insecure-kubelet-readonly-port)`] [`[--enable-intra-node-visibility](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-intra-node-visibility)`] [`[--enable-ip-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-ip-access)`] [`[--enable-ip-alias](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-ip-alias)`] [`[--enable-kubernetes-alpha](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-kubernetes-alpha)`] [`[--enable-kubernetes-unstable-apis](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-kubernetes-unstable-apis)`=`API`,[`[API](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#API)`,…]] [`[--enable-l4-ilb-subsetting](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-l4-ilb-subsetting)`] [`[--enable-legacy-authorization](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-legacy-authorization)`] [`[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-managed-prometheus)`] [`[--enable-master-global-access](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-master-global-access)`] [`[--enable-multi-networking](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-multi-networking)`] [`[--enable-nested-virtualization](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-nested-virtualization)`] [`[--enable-network-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-network-policy)`] [`[--enable-ray-cluster-logging](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-ray-cluster-logging)`] [`[--enable-ray-cluster-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-ray-cluster-monitoring)`] [`[--enable-secret-manager](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-secret-manager)`] [`[--enable-service-externalips](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-service-externalips)`] [`[--enable-shielded-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-shielded-nodes)`] [`[--enable-stackdriver-kubernetes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-stackdriver-kubernetes)`] [`[--enable-vertical-pod-autoscaling](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-vertical-pod-autoscaling)`] [`[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--fleet-project)`=`PROJECT_ID_OR_NUMBER`] [`[--gateway-api](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--gateway-api)`=`GATEWAY_API`] [`[--hpa-profile](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--hpa-profile)`=`HPA_PROFILE`] [`[--image-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--image-type)`=`IMAGE_TYPE`] [`[--in-transit-encryption](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--in-transit-encryption)`=`IN_TRANSIT_ENCRYPTION`] [`[--ipv6-access-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--ipv6-access-type)`=`IPV6_ACCESS_TYPE`] [`[--issue-client-certificate](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--issue-client-certificate)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--logging)`=[`COMPONENT`,…]] [`[--logging-variant](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--logging-variant)`=`LOGGING_VARIANT`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--machine-type)`=`MACHINE_TYPE`, `[-m](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#-m)` `[MACHINE_TYPE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#MACHINE_TYPE)`] [`[--max-nodes-per-pool](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-nodes-per-pool)`=`MAX_NODES_PER_POOL`] [`[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE`] [`[--max-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-surge-upgrade)`=`MAX_SURGE_UPGRADE`; default=1] [`[--max-unavailable-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-unavailable-upgrade)`=`MAX_UNAVAILABLE_UPGRADE`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#KEY)`=`VALUE`,…]] [`[--metadata-from-file](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--metadata-from-file)`=`KEY`=`LOCAL_FILE_PATH`,[…]] [`[--min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-cpu-platform)`=`PLATFORM`] [`[--monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--monitoring)`=[`COMPONENT`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--network)`=`NETWORK`] [`[--network-performance-configs](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--network-performance-configs)`=[`PROPERTY1`=`VALUE1`,…]] [`[--node-labels](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-labels)`=[`NODE_LABEL`,…]] [`[--node-locations](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-locations)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#ZONE)`,…]] [`[--node-taints](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-taints)`=[`NODE_TAINT`,…]] [`[--node-version](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-version)`=`NODE_VERSION`] [`[--notification-config](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--notification-config)`=[`pubsub`=`ENABLED`|`[DISABLED](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#DISABLED)`,`pubsub-topic`=`TOPIC`,…]] [`[--num-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--num-nodes)`=`NUM_NODES`; default=3] [`[--placement-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--placement-policy)`=`PLACEMENT_POLICY`] [`[--placement-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--placement-type)`=`PLACEMENT_TYPE`] [`[--preemptible](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--preemptible)`] [`[--private-endpoint-subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--private-endpoint-subnetwork)`=`NAME`] [`[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`] [`[--release-channel](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--release-channel)`=[`CHANNEL`]] [`[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--resource-manager-tags)`=[`KEY`=`VALUE`,…]] [`[--security-group](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--security-group)`=`SECURITY_GROUP`] [`[--security-posture](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--security-posture)`=`SECURITY_POSTURE`] [`[--services-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--services-ipv4-cidr)`=`CIDR`] [`[--services-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--services-secondary-range-name)`=`NAME`] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--shielded-secure-boot)`] [`[--spot](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--spot)`] [`[--stack-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--stack-type)`=`STACK_TYPE`] [`[--storage-pools](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--storage-pools)`=`STORAGE_POOL`,[…]] [`[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--subnetwork)`=`SUBNETWORK`] [`[--system-config-from-file](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--system-config-from-file)`=`PATH_TO_FILE`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#TAG)`,…]] [`[--threads-per-core](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--threads-per-core)`=`THREADS_PER_CORE`] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--tier)`=`TIER`] [`[--workload-metadata](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--workload-metadata)`=`WORKLOAD_METADATA`] [`[--workload-pool](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--workload-pool)`=`WORKLOAD_POOL`] [`[--workload-vulnerability-scanning](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--workload-vulnerability-scanning)`=`WORKLOAD_VULNERABILITY_SCANNING`] [`[--aggregation-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--aggregation-ca)`=`CA_POOL_PATH` `[--cluster-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-ca)`=`CA_POOL_PATH` `[--control-plane-disk-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--control-plane-disk-encryption-key)`=`KEY` `[--etcd-api-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--etcd-api-ca)`=`CA_POOL_PATH` `[--etcd-peer-ca](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--etcd-peer-ca)`=`CA_POOL_PATH` `[--gkeops-etcd-backup-encryption-key](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--gkeops-etcd-backup-encryption-key)`=`KEY` `[--service-account-signing-keys](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--service-account-signing-keys)`=`KEY_VERSION`,[`[KEY_VERSION](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#KEY_VERSION)`,…] `[--service-account-verification-keys](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--service-account-verification-keys)`=`KEY_VERSION`,[`[KEY_VERSION](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#KEY_VERSION)`,…]] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`     | `[--enable-binauthz](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-binauthz)`] [`[--cluster-dns](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-dns)`=`CLUSTER_DNS` `[--cluster-dns-domain](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-dns-domain)`=`CLUSTER_DNS_DOMAIN` `[--cluster-dns-scope](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--cluster-dns-scope)`=`CLUSTER_DNS_SCOPE` `[--additive-vpc-scope-dns-domain](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--additive-vpc-scope-dns-domain)`=`ADDITIVE_VPC_SCOPE_DNS_DOMAIN`     | `[--disable-additive-vpc-scope](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-additive-vpc-scope)`] [`[--dataplane-v2-observability-mode](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--dataplane-v2-observability-mode)`=`DATAPLANE_V2_OBSERVABILITY_MODE`     | `[--disable-dataplane-v2-flow-observability](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-dataplane-v2-flow-observability)`     | `[--enable-dataplane-v2-flow-observability](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-dataplane-v2-flow-observability)`] [`[--disable-dataplane-v2-metrics](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disable-dataplane-v2-metrics)`     | `[--enable-dataplane-v2-metrics](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-dataplane-v2-metrics)`] [[`[--enable-autoprovisioning](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoprovisioning)` : `[--autoprovisioning-config-file](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-config-file)`=`PATH_TO_FILE` | [`[--max-cpu](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-cpu)`=`MAX_CPU` `[--max-memory](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-memory)`=`MAX_MEMORY` : `[--autoprovisioning-image-type](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-image-type)`=`AUTOPROVISIONING_IMAGE_TYPE` `[--autoprovisioning-locations](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-locations)`=`ZONE`,[`[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#ZONE)`,…] `[--autoprovisioning-min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-min-cpu-platform)`=`PLATFORM` `[--min-cpu](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-cpu)`=`MIN_CPU` `[--min-memory](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-memory)`=`MIN_MEMORY` `[--autoprovisioning-max-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-max-surge-upgrade)`=`AUTOPROVISIONING_MAX_SURGE_UPGRADE` `[--autoprovisioning-max-unavailable-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-max-unavailable-upgrade)`=`AUTOPROVISIONING_MAX_UNAVAILABLE_UPGRADE` `[--autoprovisioning-node-pool-soak-duration](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-node-pool-soak-duration)`=`AUTOPROVISIONING_NODE_POOL_SOAK_DURATION` `[--autoprovisioning-standard-rollout-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-standard-rollout-policy)`=[`batch-node-count`=`BATCH_NODE_COUNT`,`batch-percent`=`BATCH_NODE_PERCENTAGE`,`batch-soak-duration`=`BATCH_SOAK_DURATION`,…] `[--enable-autoprovisioning-blue-green-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoprovisioning-blue-green-upgrade)` | `[--enable-autoprovisioning-surge-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoprovisioning-surge-upgrade)` `[--autoprovisioning-scopes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-scopes)`=[`SCOPE`,…] `[--autoprovisioning-service-account](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-service-account)`=`AUTOPROVISIONING_SERVICE_ACCOUNT` `[--enable-autoprovisioning-autorepair](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoprovisioning-autorepair)` `[--enable-autoprovisioning-autoupgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoprovisioning-autoupgrade)` [`[--max-accelerator](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-accelerator)`=[`type`=`TYPE`,`count`=`COUNT`,…] : `[--min-accelerator](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-accelerator)`=[`type`=`TYPE`,`count`=`COUNT`,…]]]]] [`[--enable-autoscaling](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-autoscaling)` `[--location-policy](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--location-policy)`=`LOCATION_POLICY` `[--max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--max-nodes)`=`MAX_NODES` `[--min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-nodes)`=`MIN_NODES` `[--total-max-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--total-max-nodes)`=`TOTAL_MAX_NODES` `[--total-min-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--total-min-nodes)`=`TOTAL_MIN_NODES`] [`[--enable-insecure-binding-system-authenticated](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-insecure-binding-system-authenticated)` `[--enable-insecure-binding-system-unauthenticated](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-insecure-binding-system-unauthenticated)`] [`[--enable-master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-master-authorized-networks)` `[--master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--master-authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#NETWORK)`,…]] [`[--enable-network-egress-metering](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-network-egress-metering)` `[--enable-resource-consumption-metering](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-resource-consumption-metering)` `[--resource-usage-bigquery-dataset](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--resource-usage-bigquery-dataset)`=`RESOURCE_USAGE_BIGQUERY_DATASET`] [`[--enable-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-private-endpoint)` `[--enable-private-nodes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-private-nodes)` `[--master-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--master-ipv4-cidr)`=`MASTER_IPV4_CIDR`] [`[--ephemeral-storage-local-ssd](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--ephemeral-storage-local-ssd)`[=[`count`=`COUNT`]]     | `[--local-nvme-ssd-block](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--local-nvme-ssd-block)`[=[`count`=`COUNT`]]     | `[--local-ssd-count](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--local-ssd-count)`=`LOCAL_SSD_COUNT`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#ZONE)`] [`[--maintenance-window](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--maintenance-window)`=`START_TIME`     | `[--maintenance-window-end](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--maintenance-window-end)`=`TIME_STAMP` `[--maintenance-window-recurrence](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--maintenance-window-recurrence)`=`RRULE` `[--maintenance-window-start](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--maintenance-window-start)`=`TIME_STAMP`] [`[--password](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--password)`=`PASSWORD` `[--enable-basic-auth](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--enable-basic-auth)`     | `[--username](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--username)`=`USERNAME`, `[-u](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#-u)` `[USERNAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#USERNAME)`] [`[--reservation](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--reservation-affinity)`=`RESERVATION_AFFINITY`] [`[--scopes](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--scopes)`=[`SCOPE`,…]; default="gke-default" `[--service-account](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--service-account)`=`SERVICE_ACCOUNT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a cluster for running containers.

**EXAMPLES**

: To create a cluster with the default configuration, run:

```
gcloud container clusters create sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of the cluster to create.
The name may contain only lowercase alphanumerics and '-', must start with a
letter and end with an alphanumeric, and must be no longer than 40 characters.

**FLAGS**

: **--accelerator**:
Attaches accelerators (e.g. GPUs) to all nodes.

**`type`**:
(Required) The specific type (e.g. nvidia-tesla-t4 for NVIDIA T4) of accelerator
to attach to the instances. Use `gcloud compute accelerator-types
list` to learn about all available accelerator types.

**`count`**:
(Optional) The number of accelerators to attach to the instances. The default
value is 1.

**`gpu-driver-version`**:
(Optional) The NVIDIA driver version to install. GPU_DRIVER_VERSION must be one
of:

```
`default`: Install the default driver version for this GKE version.
```

```
`latest`: Install the latest driver version available for this GKE version.
Can only be used for nodes that use Container-Optimized OS.
```

```
`disabled`: Skip automatic driver installation. You must manually install a
driver after you create the cluster. If you omit the flag `gpu-driver-version`,
this is the default option. To learn how to manually install the GPU driver,
refer to: https://cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers
```

**`gpu-partition-size`**:
(Optional) The GPU partition size used when running multi-instance GPUs. For
information about multi-instance GPUs, refer to: [https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi](https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi)

**`gpu-sharing-strategy`**:
(Optional) The GPU sharing strategy (e.g. time-sharing) to use. For information
about GPU sharing, refer to: [https://cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus](https://cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus)

**`max-shared-clients-per-gpu`**:
(Optional) The max number of containers allowed to share each GPU on the node.
This field is used together with `gpu-sharing-strategy`.

**--additional-zones**:
(DEPRECATED) The set of additional zones in which the specified node footprint
should be replicated. All zones must be in the same region as the cluster's
primary zone. If additional-zones is not specified, all nodes will be in the
cluster's primary zone.
Note that `NUM_NODES` nodes will be created in each zone, such that
if you specify `--num-nodes=4` and choose one additional zone, 8
nodes will be created.
Multiple locations can be specified, separated by commas. For example:

```
gcloud container clusters create example-cluster --zone us-central1-a --additional-zones us-central1-b,us-central1-c
```

This flag is deprecated. Use --node-locations=PRIMARY_ZONE,[ZONE,…]
instead.

**--addons**:
Addons
(https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.AddonsConfig)
are additional Kubernetes cluster components. Addons specified by this flag will
be enabled. The others will be disabled. Default addons: HttpLoadBalancing,
HorizontalPodAutoscaling. The Istio addon is deprecated and removed. For more
information and migration, see [https://cloud.google.com/istio/docs/istio-on-gke/migrate-to-anthos-service-mesh](https://cloud.google.com/istio/docs/istio-on-gke/migrate-to-anthos-service-mesh).
ADDON must be one of: HttpLoadBalancing, HorizontalPodAutoscaling,
KubernetesDashboard, NetworkPolicy, NodeLocalDNS, ConfigConnector,
GcePersistentDiskCsiDriver, GcpFilestoreCsiDriver, BackupRestore,
GcsFuseCsiDriver, ParallelstoreCsiDriver, RayOperator, CloudRun.

**--anonymous-authentication-config**:
Enable or restrict anonymous access to the cluster. When enabled, anonymous
users will be authenticated as system:anonymous with the group
system:unauthenticated. Limiting access restricts anonymous access to only the
health check endpoints /readyz, /livez, and /healthz.
`ANONYMOUS_AUTHENTICATION_CONFIG` must be one of:

**`ENABLED`**:
'ENABLED' enables anonymous calls.

**`LIMITED`**:
'LIMITED' restricts anonymous access to the cluster. Only calls to the health
check endpoints are allowed anonymously, all other calls will be rejected.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-monitoring-scope**:
Enables Auto-Monitoring for a specific scope within the cluster. ALL: Enables
Auto-Monitoring for all supported workloads within the cluster. NONE: Disables
Auto-Monitoring. `AUTO_MONITORING_SCOPE` must be one of:
`ALL`, `NONE`.

**--autoprovisioning-enable-insecure-kubelet-readonly-port**:
Enables the Kubelet's insecure read only port for Autoprovisioned Node Pools.
If not set, the value from nodePoolDefaults.nodeConfigDefaults will be used.
To disable the readonly port
`--no-autoprovisioning-enable-insecure-kubelet-readonly-port`.

**--autoprovisioning-network-tags**:
Applies the given Compute Engine tags (comma separated) on all nodes in the
auto-provisioned node pools of the new Standard cluster or the new Autopilot
cluster.
Examples:

```
gcloud container clusters create example-cluster --autoprovisioning-network-tags=tag1,tag2
```

New nodes in auto-provisioned node pools, including ones created by resize or
recreate, will have these tags on the Compute Engine API instance object and can
be used in firewall rules. See [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)
for examples.

**--autoprovisioning-resource-manager-tags**:
Applies the specified comma-separated resource manager tags that has the
GCE_FIREWALL purpose to all nodes in the new Autopilot cluster or all
auto-provisioned nodes in the new Standard cluster.
Examples:

```
gcloud container clusters create example-cluster --autoprovisioning-resource-manager-tags=tagKeys/1234=tagValues/2345
gcloud container clusters create example-cluster --autoprovisioning-resource-manager-tags=my-project/key1=value1
gcloud container clusters create example-cluster --autoprovisioning-resource-manager-tags=12345/key1=value1,23456/key2=value2
gcloud container clusters create example-cluster --autoprovisioning-resource-manager-tags=
```

All nodes in an Autopilot cluster or all auto-provisioned nodes in a Standard
cluster, including nodes that are resized or re-created, will have the specified
tags on the corresponding Instance object in the Compute Engine API. You can
reference these tags in network firewall policy rules. For instructions, see [https://cloud.google.com/firewall/docs/use-tags-for-firewalls](https://cloud.google.com/firewall/docs/use-tags-for-firewalls).

**--autoscaling-profile**:
Set autoscaling behaviour, choices are 'optimize-utilization' and 'balanced'.
Default is 'balanced'.

**--boot-disk-kms-key**:
The Customer Managed Encryption Key used to encrypt the boot disk attached to
each node in the node pool. This should be of the form
projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME].
For more information about protecting resources with Cloud KMS Keys please see:
[https://cloud.google.com/compute/docs/disks/customer-managed-encryption](https://cloud.google.com/compute/docs/disks/customer-managed-encryption)

**--cloud-run-config**:
Configurations for Cloud Run addon, requires `--addons=CloudRun` for
create and `--update-addons=CloudRun=ENABLED` for update.

**`load-balancer-type`**:
(Optional) Type of load-balancer-type EXTERNAL or INTERNAL.
Examples:

```
gcloud container clusters create example-cluster --cloud-run-config=load-balancer-type=INTERNAL
```

**--cluster-ipv4-cidr**:
The IP address range for the pods in this cluster in CIDR notation (e.g.
10.0.0.0/14). Prior to Kubernetes version 1.7.0 this must be a subset of
10.0.0.0/8; however, starting with version 1.7.0 can be any RFC 1918 IP range.
If you omit this option, a range is chosen automatically. The automatically
chosen range is randomly selected from 10.0.0.0/8 and will not include IP
address ranges allocated to VMs, existing routes, or ranges allocated to other
clusters. The automatically chosen range might conflict with reserved IP
addresses, dynamic routes, or routes within VPCs that peer with this cluster.
You should specify `--cluster-ipv4-cidr` to prevent conflicts.
This field is not applicable in a Shared VPC setup where the IP address range
for the pods must be specified with `--cluster-secondary-range-name`

**--cluster-secondary-range-name**:
Set the secondary range to be used as the source for pod IPs. Alias ranges will
be allocated from this secondary range. NAME must be the name of an existing
secondary range in the cluster subnetwork.
Cannot be specified unless '--enable-ip-alias' option is also specified. Cannot
be used with '--create-subnetwork' option.

**--cluster-version**:
The Kubernetes version to use for the master and nodes. Defaults to
server-specified.
The default Kubernetes version is available using the following command.

```
gcloud container get-server-config
```

**--confidential-node-type**:
Enable confidential nodes for the cluster. Enabling Confidential Nodes will
create nodes using Confidential VM [https://cloud.google.com/compute/confidential-vm/docs/about-cvm](https://cloud.google.com/compute/confidential-vm/docs/about-cvm).
`CONFIDENTIAL_NODE_TYPE` must be one of: `sev`,
`sev_snp`, `tdx`.

**--containerd-config-from-file**:
Path of the YAML file that contains containerd configuration entries like
configuring access to private image registries.
For detailed information on the configuration usage, please refer to [https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration](https://cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
Note: Updating the containerd configuration of an existing cluster or node pool
requires recreation of the existing nodes, which might cause disruptions in
running workloads.
Use a full or relative path to a local file containing the value of
containerd_config.

**--create-subnetwork**:
Create a new subnetwork for the cluster. The name and range of the subnetwork
can be customized via optional 'name' and 'range' key-value pairs.
'name' specifies the name of the subnetwork to be created.
'range' specifies the IP range for the new subnetwork. This can either be a
netmask size (e.g. '/20') or a CIDR range (e.g. '10.0.0.0/20'). If a netmask
size is specified, the IP is automatically taken from the free space in the
cluster's network.
Examples:
Create a new subnetwork with a default name and size.

```
gcloud container clusters create --create-subnetwork ""
```

Create a new subnetwork named "my-subnet" with netmask of size 21.

```
gcloud container clusters create --create-subnetwork name=my-subnet,range=/21
```

Create a new subnetwork with a default name with the primary range of
10.100.0.0/16.

```
gcloud container clusters create --create-subnetwork range=10.100.0.0/16
```

Create a new subnetwork with the name "my-subnet" with a default range.

```
gcloud container clusters create --create-subnetwork name=my-subnet
```

Cannot be specified unless '--enable-ip-alias' option is also specified. Cannot
be used in conjunction with '--subnetwork' option.

**--data-cache-count**:
Specifies the number of local SSDs to be utilized for GKE Data Cache in the
cluster.

**--database-encryption-key**:
Enable Database Encryption.
Enable database encryption that will be used to encrypt Kubernetes Secrets at
the application layer. The key provided should be the resource ID in the format
of
`projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]`.
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets](https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

**--default-max-pods-per-node**:
The default max number of pods per node for node pools in the cluster.
This flag sets the default max-pods-per-node for node pools in the cluster. If
--max-pods-per-node is not specified explicitly for a node pool, this flag value
will be used.
Must be used in conjunction with '--enable-ip-alias'.

**--disable-default-snat**:
Disable default source NAT rules applied in cluster nodes.
By default, cluster nodes perform source network address translation (SNAT) for
packets sent from Pod IP address sources to destination IP addresses that are
not in the non-masquerade CIDRs list. For more details about SNAT and IP
masquerading, see: [https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#how_ipmasq_works](https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#how_ipmasq_works)
SNAT changes the packet's source IP address to the node's internal IP address.
When this flag is set, GKE does not perform SNAT for packets sent to any
destination. You must set this flag if the cluster uses privately reused public
IPs.
The --disable-default-snat flag is only applicable to private GKE clusters,
which are inherently VPC-native. Thus, --disable-default-snat requires that you
also set --enable-ip-alias and --enable-private-nodes.

**--disable-l4-lb-firewall-reconciliation**:
Disable reconciliation on the cluster for L4 Load Balancer VPC firewalls
targeting ingress traffic.

**--disk-size**:
Size for node VM boot disks in GB. Defaults to 100GB.

**--disk-type**:
Type of the node VM boot disk. For version 1.24 and later, defaults to
pd-balanced. For versions earlier than 1.24, defaults to pd-standard.
`DISK_TYPE` must be one of: `pd-standard`,
`pd-ssd`, `pd-balanced`, `hyperdisk-balanced`,
`hyperdisk-extreme`, `hyperdisk-throughput`.

**--enable-authorized-networks-on-private-endpoint**:
Enable enforcement of --master-authorized-networks CIDR ranges for traffic
reaching cluster's control plane via private IP.

**--enable-autorepair**:
Enable node autorepair feature for a cluster's default node pool(s).

```
gcloud container clusters create example-cluster --enable-autorepair
```

Node autorepair is enabled by default for clusters using COS, COS_CONTAINERD,
UBUNTU or UBUNTU_CONTAINERD as a base image, use --no-enable-autorepair to
disable.
See [https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair](https://cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)
for more info.

**--enable-autoupgrade**:
Sets autoupgrade feature for a cluster's default node pool(s).

```
gcloud container clusters create example-cluster --enable-autoupgrade
```

See [https://cloud.google.com/kubernetes-engine/docs/node-auto-upgrades](https://cloud.google.com/kubernetes-engine/docs/node-auto-upgrades)
for more info.
Enabled by default, use `--no-enable-autoupgrade` to disable.

**--enable-cilium-clusterwide-network-policy**:
Enable Cilium Clusterwide Network Policies on the cluster. Disabled by default.

**--enable-cloud-logging**:
(DEPRECATED) Automatically send logs from the cluster to the Google Cloud
Logging API.
Legacy Logging and Monitoring is deprecated. Thus, flag
`--enable-cloud-logging` is also deprecated and will be removed in an
upcoming release. Please use `--logging` (optionally with
`--monitoring`). For more details, please read: [https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs)
and [https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics).

**--enable-cloud-monitoring**:
(DEPRECATED) Automatically send metrics from pods in the cluster to the Google
Cloud Monitoring API. VM metrics will be collected by Google Compute Engine
regardless of this setting.
Legacy Logging and Monitoring is deprecated. Thus, flag
`--enable-cloud-monitoring` is also deprecated. Please use
`--monitoring` (optionally with `--logging`). For more
details, please read: [https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics)
and [https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs).

**--enable-cloud-run-alpha**:
Enable Cloud Run alpha features on this cluster. Selecting this option will
result in the cluster having all Cloud Run alpha API groups and features turned
on.
Cloud Run alpha clusters are not covered by the Cloud Run SLA and should not be
used for production workloads.

**--enable-confidential-nodes**:
Enable confidential nodes for the cluster. Enabling Confidential Nodes will
create nodes using Confidential VM [https://cloud.google.com/compute/confidential-vm/docs/about-cvm](https://cloud.google.com/compute/confidential-vm/docs/about-cvm).

**--enable-confidential-storage**:
Enable confidential storage for the cluster. Enabling Confidential Storage will
create boot disk with confidential mode

**--enable-cost-allocation**:
Enable the cost management feature.
When enabled, you can get informational GKE cost breakdowns by cluster,
namespace and label in your billing data exported to BigQuery
(https://cloud.google.com/billing/docs/how-to/export-data-bigquery).

**--enable-dataplane-v2**:
Enables the new eBPF dataplane for GKE clusters that is required for network
security, scalability and visibility features.

**--enable-dns-access**:
Enable access to the cluster's control plane over DNS-based endpoint.
DNS-based control plane access is recommended.

**--enable-fleet**:
Set cluster project as the fleet host project. This will register the cluster to
the same project. To register the cluster to a fleet in a different project,
please use `--fleet-project=FLEET_HOST_PROJECT`. Example: $ gcloud
container clusters create --enable-fleet

**--enable-fqdn-network-policy**:
Enable FQDN Network Policies on the cluster. FQDN Network Policies are disabled
by default.

**--enable-google-cloud-access**:
When you enable Google Cloud Access, any public IP addresses owned by Google
Cloud can reach the public control plane endpoint of your cluster.

**--enable-gvnic**:
Enable the use of GVNIC for this cluster. Requires re-creation of nodes using
either a node-pool upgrade or node-pool creation.

**--enable-identity-service**:
Enable Identity Service component on the cluster.
When enabled, users can authenticate to Kubernetes cluster with external
identity providers.
Identity Service is by default disabled when creating a new cluster. To disable
Identity Service in an existing cluster, explicitly set flag
`--no-enable-identity-service`.

**--enable-image-streaming**:
Specifies whether to enable image streaming on cluster.

**--enable-insecure-kubelet-readonly-port**:
Enables the Kubelet's insecure read only port.
To disable the readonly port on a cluster or node-pool set the flag to
`--no-enable-insecure-kubelet-readonly-port`.

**--enable-intra-node-visibility**:
Enable Intra-node visibility for this cluster.
Enabling intra-node visibility makes your intra-node pod-to-pod traffic visible
to the networking fabric. With this feature, you can use VPC flow logging or
other VPC features for intra-node traffic.
Enabling it on an existing cluster causes the cluster master and the cluster
nodes to restart, which might cause a disruption.

**--enable-ip-access**:
Enable access to the cluster's control plane over private IP and public IP if
--enable-private-endpoint is not enabled.

**--enable-ip-alias**:
--enable-ip-alias creates a VPC-native cluster. If you set this option, you can
optionally specify the IP address ranges to use for Pods and Services. For
instructions, see [https://cloud.google.com/kubernetes-engine/docs/how-to/alias-ips](https://cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
--no-enable-ip-alias creates a routes-based cluster. This type of cluster routes
traffic between Pods using Google Cloud Routes. This option is not recommended;
use the default VPC-native cluster type instead. For instructions, see [https://cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster)
You can't specify both --enable-ip-alias and --no-enable-ip-alias. If you omit
both --enable-ip-alias and --no-enable-ip-alias, the default is a VPC-native
cluster.

**--enable-kubernetes-alpha**:
Enable Kubernetes alpha features on this cluster. Selecting this option will
result in the cluster having all Kubernetes alpha API groups and features turned
on. Cluster upgrades (both manual and automatic) will be disabled and the
cluster will be automatically deleted after 30 days.
Alpha clusters are not covered by the Kubernetes Engine SLA and should not be
used for production workloads.

**--enable-kubernetes-unstable-apis**:
Enable Kubernetes beta API features on this cluster. Beta APIs are not expected
to be production ready and should be avoided in production-grade environments.

**--enable-l4-ilb-subsetting**:
Enable Subsetting for L4 ILB services created on this cluster.

**--enable-legacy-authorization**:
Enables the legacy ABAC authentication for the cluster. User rights are granted
through the use of policies which combine attributes together. For a detailed
look at these properties and related formats, see [https://kubernetes.io/docs/admin/authorization/abac/](https://kubernetes.io/docs/admin/authorization/abac/).
To use RBAC permissions instead, create or update your cluster with the option
`--no-enable-legacy-authorization`.

**--enable-managed-prometheus**:
Enables managed collection for Managed Service for Prometheus in the cluster.
See [https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke)
for more info.
Enabled by default for cluster versions 1.27 or greater, use
--no-enable-managed-prometheus to disable.

**--enable-master-global-access**:
Use with private clusters to allow access to the master's private endpoint from
any Google Cloud region or on-premises environment regardless of the private
cluster's region.

**--enable-multi-networking**:
Enables multi-networking on the cluster. Multi-networking is disabled by
default.

**--enable-nested-virtualization**:
Enables the use of nested virtualization on the default initial node pool.
Defaults to `false`. Can only be enabled on UBUNTU_CONTAINERD base
image or COS_CONTAINERD base image with version 1.28.4-gke.1083000 and above.

**--enable-network-policy**:
Enable network policy enforcement for this cluster. If you are enabling network
policy on an existing cluster the network policy addon must first be enabled on
the master by using --update-addons=NetworkPolicy=ENABLED flag.

**--enable-ray-cluster-logging**:
Enable automatic log processing sidecar for Ray clusters.

**--enable-ray-cluster-monitoring**:
Enable automatic metrics collection for Ray clusters.

**--enable-secret-manager**

**--enable-service-externalips**:
Enables use of services with externalIPs field.

**--enable-shielded-nodes**:
Enable Shielded Nodes for this cluster. Enabling Shielded Nodes will enable a
more secure Node credential bootstrapping implementation. Starting with version
1.18, clusters will have Shielded GKE nodes by default.

**--enable-stackdriver-kubernetes**:
(DEPRECATED) Enable Cloud Operations for GKE.
The `--enable-stackdriver-kubernetes` flag is deprecated and will be
removed in an upcoming release. Please use `--logging` and
`--monitoring` instead. For more information, please read: [https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs)
and [https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics).

**--enable-vertical-pod-autoscaling**

**--fleet-project**:
Sets fleet host project for the cluster. If specified, the current cluster will
be registered as a fleet membership under the fleet host project.
Example: $ gcloud container clusters create --fleet-project=my-project

**--gateway-api**:
Enables GKE Gateway controller in this cluster. The value of the flag specifies
which Open Source Gateway API release channel will be used to define Gateway
resources. `GATEWAY_API` must be one of:

**`disabled`**:
Gateway controller will be disabled in the cluster.

**`standard`**:
Gateway controller will be enabled in the cluster. Resource definitions from the
`standard` OSS Gateway API release channel will be installed.

**--hpa-profile**:
Set Horizontal Pod Autoscaler behavior. Accepted values are: none, performance.
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile](https://cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#hpa-profile).

**--image-type**:
The image type to use for the cluster. Defaults to server-specified.
Image Type specifies the base OS that the nodes in the cluster will run on. If
an image type is specified, that will be assigned to the cluster and all future
upgrades will use the specified image type. If it is not specified the server
will pick the default image type.
The default image type and the list of valid image types are available using the
following command.

```
gcloud container get-server-config
```

**--in-transit-encryption**:
Enable Dataplane V2 in-transit encryption. Dataplane v2 in-transit encryption is
disabled by default. `IN_TRANSIT_ENCRYPTION` must be one
of: `inter-node-transparent`, `none`.

**--ipv6-access-type**:
IPv6 access type of the subnetwork. Defaults to 'external'.
`IPV6_ACCESS_TYPE` must be one of: `external`,
`internal`.

**--issue-client-certificate**:
Issue a TLS client certificate with admin permissions.
When enabled, the certificate and private key pair will be present in MasterAuth
field of the Cluster object. For cluster versions before 1.12, a client
certificate will be issued by default. As of 1.12, client certificates are
disabled by default.

**--labels**:
Labels to apply to the Google Cloud resources in use by the Kubernetes Engine
cluster. These are unrelated to Kubernetes labels.
Examples:

```
gcloud container clusters create example-cluster --labels=label_a=value1,label_b=,label_c=value3
```

**--logging**:
Set the components that have logging enabled. Valid component values are:
`SYSTEM`, `WORKLOAD`, `API_SERVER`,
`CONTROLLER_MANAGER`, `SCHEDULER`, `NONE`
For more information, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs](https://cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
Examples:

```
gcloud container clusters create --logging=SYSTEM
gcloud container clusters create --logging=SYSTEM,API_SERVER,WORKLOAD
gcloud container clusters create --logging=NONE
```

**--logging-variant**:
Specifies the logging variant that will be deployed on all the nodes in the
cluster. Valid logging variants are `MAX_THROUGHPUT`,
`DEFAULT`. If no value is specified, DEFAULT is used.
`LOGGING_VARIANT` must be one of:

**`DEFAULT`**:
'DEFAULT' variant requests minimal resources but may not guarantee high
throughput.

**`MAX_THROUGHPUT`**:
'MAX_THROUGHPUT' variant requests more node resources and is able to achieve
logging throughput up to 10MB per sec.

**--machine-type**:
The type of machine to use for nodes. Defaults to e2-medium. The list of
predefined machine types is available using the following command:

```
gcloud compute machine-types list
```

You can also specify custom machine types by providing a string with the format
"custom-CPUS-RAM" where "CPUS" is the number of virtual CPUs and "RAM" is the
amount of RAM in MiB.
For example, to create a node pool using custom machines with 2 vCPUs and 12 GB
of RAM:

```
gcloud container clusters create high-mem-pool --machine-type=custom-2-12288
```

**--max-nodes-per-pool**:
The maximum number of nodes to allocate per default initial node pool.
Kubernetes Engine will automatically create enough nodes pools such that each
node pool contains less than `--max-nodes-per-pool` nodes. Defaults
to 1000 nodes, but can be set as low as 100 nodes per pool on initial create.

**--max-pods-per-node**:
The max number of pods per node for this node pool.
This flag sets the maximum number of pods that can be run at the same time on a
node. This will override the value given with --default-max-pods-per-node flag
set at the cluster level.
Must be used in conjunction with '--enable-ip-alias'.

**--max-surge-upgrade**:
Number of extra (surge) nodes to be created on each upgrade of a node pool.
Specifies the number of extra (surge) nodes to be created during this node
pool's upgrades. For example, running the following command will result in
creating an extra node each time the node pool is upgraded:

```
gcloud container clusters create example-cluster --max-surge-upgrade=1 --max-unavailable-upgrade=0
```

Must be used in conjunction with '--max-unavailable-upgrade'.

**--max-unavailable-upgrade**:
Number of nodes that can be unavailable at the same time on each upgrade of a
node pool.
Specifies the number of nodes that can be unavailable at the same time while
this node pool is being upgraded. For example, running the following command
will result in having 3 nodes being upgraded in parallel (1 + 2), but keeping
always at least 3 (5 - 2) available each time the node pool is upgraded:

```
gcloud container clusters create example-cluster --num-nodes=5 --max-surge-upgrade=1      --max-unavailable-upgrade=2
```

Must be used in conjunction with '--max-surge-upgrade'.

**--metadata**:
Compute Engine metadata to be made available to the guest operating system
running on nodes within the node pool.
Each metadata entry is a key/value pair separated by an equals sign. Metadata
keys must be unique and less than 128 bytes in length. Values must be less than
or equal to 32,768 bytes in length. The total size of all keys and values must
be less than 512 KB. Multiple arguments can be passed to this flag. For example:
``--metadata
key-1=value-1,key-2=value-2,key-3=value-3``
Additionally, the following keys are reserved for use by Kubernetes Engine:

- ``cluster-location``
- ``cluster-name``
- ``cluster-uid``
- ``configure-sh``
- ``enable-os-login``
- ``gci-update-strategy``
- ``gci-ensure-gke-docker``
- ``instance-template``
- ``kube-env``
- ``startup-script``
- ``user-data``

Google Kubernetes Engine sets the following keys by default:

- ``serial-port-logging-enable``

See also Compute Engine's [documentation](https://cloud.google.com/compute/docs/storing-retrieving-metadata)
on storing and retrieving instance metadata.

**--metadata-from-file**:
Same as ``--metadata`` except that the value
for the entry will be read from a local file.

**--min-cpu-platform**:
When specified, the nodes for the new cluster's default node pool will be
scheduled on host with specified CPU architecture or a newer one.
Examples:

```
gcloud container clusters create example-cluster --min-cpu-platform=PLATFORM
```

To list available CPU platforms in given zone, run:

```
gcloud beta compute zones describe ZONE --format="value(availableCpuPlatforms)"
```

CPU platform selection is available only in selected zones.

**--monitoring**:
Set the components that have monitoring enabled. Valid component values are:
`SYSTEM`, `WORKLOAD` (Deprecated), `NONE`,
`API_SERVER`, `CONTROLLER_MANAGER`,
`SCHEDULER`, `DAEMONSET`, `DEPLOYMENT`,
`HPA`, `POD`, `STATEFULSET`,
`STORAGE`, `CADVISOR`, `KUBELET`,
`DCGM`, `JOBSET`
For more information, see [https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics](https://cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#available-metrics)
Examples:

```
gcloud container clusters create --monitoring=SYSTEM,API_SERVER,POD
gcloud container clusters create --monitoring=NONE
```

**--network**:
The Compute Engine Network that the cluster will connect to. Google Kubernetes
Engine will use this network when creating routes and firewalls for the
clusters. Defaults to the 'default' network.

**--network-performance-configs**:
Configures network performance settings for the cluster. Node pools can override
with their own settings.

**`total-egress-bandwidth-tier`**:
Total egress bandwidth is the available outbound bandwidth from a VM, regardless
of whether the traffic is going to internal IP or external IP destinations. The
following tier values are allowed: [TIER_UNSPECIFIED,TIER_1].
See [https://cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration](https://cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)
for more information.

**--node-labels**:
Applies the given Kubernetes labels on all nodes in the new node pool.
Examples:

```
gcloud container clusters create example-cluster --node-labels=label-a=value1,label-2=value2
```

New nodes, including ones created by resize or recreate, will have these labels
on the Kubernetes API node object and can be used in nodeSelectors. See [https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
for examples.
Note that Kubernetes labels, intended to associate cluster components and
resources with one another and manage resource lifecycles, are different from
Google Kubernetes Engine labels that are used for the purpose of tracking
billing and usage information.

**--node-locations**:
The set of zones in which the specified node footprint should be replicated. All
zones must be in the same region as the cluster's master(s), specified by the
`-location`, `--zone`, or `--region` flag.
Additionally, for zonal clusters, `--node-locations` must contain the
cluster's primary zone. If not specified, all nodes will be in the cluster's
primary zone (for zonal clusters) or spread across three randomly chosen zones
within the cluster's region (for regional clusters).
Note that `NUM_NODES` nodes will be created in each zone, such that
if you specify `--num-nodes=4` and choose two locations, 8 nodes will
be created.
Multiple locations can be specified, separated by commas. For example:

```
gcloud container clusters create example-cluster --location us-central1-a --node-locations us-central1-a,us-central1-b
```

**--node-taints**:
Applies the given kubernetes taints on all nodes in default node pool(s) in new
cluster, which can be used with tolerations for pod scheduling.
Examples:

```
gcloud container clusters create example-cluster --node-taints=key1=val1:NoSchedule,key2=val2:PreferNoSchedule
```

To read more about node-taints, see [https://cloud.google.com/kubernetes-engine/docs/node-taints](https://cloud.google.com/kubernetes-engine/docs/node-taints).

**--node-version**:
The Kubernetes version to use for nodes. Defaults to server-specified.
The default Kubernetes version is available using the following command.

```
gcloud container get-server-config
```

**--notification-config**:
The notification configuration of the cluster. GKE supports publishing cluster
upgrade notifications to any Pub/Sub topic you created in the same project.
Create a subscription for the topic specified to receive notification messages.
See [https://cloud.google.com/pubsub/docs/admin](https://cloud.google.com/pubsub/docs/admin)
on how to manage Pub/Sub topics and subscriptions. You can also use the filter
option to specify which event types you'd like to receive from the following
options: SecurityBulletinEvent, UpgradeEvent, UpgradeInfoEvent,
UpgradeAvailableEvent.
Examples:

```
gcloud container clusters create example-cluster --notification-config=pubsub=ENABLED,pubsub-topic=projects/{project}/topics/{topic-name}
gcloud container clusters create example-cluster --notification-config=pubsub=ENABLED,pubsub-topic=projects/{project}/topics/{topic-name},filter="SecurityBulletinEvent|UpgradeEvent"
```

The project of the Pub/Sub topic must be the same one as the cluster. It can be
either the project ID or the project number.

**--num-nodes**:
The number of nodes to be created in each of the cluster's zones.

**--placement-policy**:
Indicates the desired resource policy to use.

```
gcloud container clusters create node-pool-1 --cluster=example-cluster --placement-policy my-placement
```

**--placement-type**:
Placement type allows to define the type of node placement within the default
node pool of this cluster.
`UNSPECIFIED` - No requirements on the placement of nodes. This is
the default option.
`COMPACT` - GKE will attempt to place the nodes in a close proximity
to each other. This helps to reduce the communication latency between the nodes,
but imposes additional limitations on the node pool size.

```
gcloud container clusters create example-cluster --placement-type=COMPACT
```

`PLACEMENT_TYPE` must be one of: `UNSPECIFIED`,
`COMPACT`.

**--preemptible**:
Create nodes using preemptible VM instances in the new cluster.

```
gcloud container clusters create example-cluster --preemptible
```

New nodes, including ones created by resize or recreate, will use preemptible VM
instances. See [https://cloud.google.com/kubernetes-engine/docs/preemptible-vm](https://cloud.google.com/kubernetes-engine/docs/preemptible-vm)
for more information on how to use Preemptible VMs with Kubernetes Engine.

**--private-endpoint-subnetwork**:
Sets the subnetwork GKE uses to provision the control plane's private endpoint.

**--private-ipv6-google-access-type**:
Sets the type of private access to Google services over IPv6.
PRIVATE_IPV6_GOOGLE_ACCESS_TYPE must be one of:

```
bidirectional
  Allows Google services to initiate connections to GKE pods in this
  cluster. This is not intended for common use, and requires previous
  integration with Google services.
```

```
disabled
  Default value. Disables private access to Google services over IPv6.
```

```
outbound-only
  Allows GKE pods to make fast, secure requests to Google services
  over IPv6. This is the most common use of private IPv6 access.
```

```
gcloud alpha container clusters create       --private-ipv6-google-access-type=disabled
gcloud alpha container clusters create       --private-ipv6-google-access-type=outbound-only
gcloud alpha container clusters create       --private-ipv6-google-access-type=bidirectional
```

`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE` must be one of:
`bidirectional`, `disabled`, `outbound-only`.

**--release-channel**:
Release channel a cluster is subscribed to.
If left unspecified and a version is specified, the cluster is enrolled in the
most mature release channel where the version is available (first checking
STABLE, then REGULAR, and finally RAPID). Otherwise, if no release channel and
no version is specified, the cluster is enrolled in the REGULAR channel with its
default version. When a cluster is subscribed to a release channel, Google
maintains both the master version and the node version. Node auto-upgrade is
enabled by default for release channel clusters and can be controlled via [upgrade-scope
exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude).
CHANNEL must be one of:
`rapid`

```
'rapid' channel is offered on an early access basis for customers
who want to test new releases.
```

```
WARNING: Versions available in the 'rapid' channel may be subject
to unresolved issues with no known workaround and are not subject
to any SLAs.
```

`regular`

```
Clusters subscribed to 'regular' receive versions that are
considered GA quality. 'regular' is intended for production users
who want to take advantage of new features.
```

`extended`

```
Clusters subscribed to 'extended' can remain on a minor version for 24 months
from when the minor version is made available in the Regular channel.
```

`stable`

```
Clusters subscribed to 'stable' receive versions that are known to
be stable and reliable in production.
```

`None`

```
Use 'None' to opt-out of any release channel.
```

`CHANNEL` must be one of: `rapid`,
`regular`, `extended`, `stable`,
`None`.

**--resource-manager-tags**:
Applies the specified comma-separated resource manager tags that has the
GCE_FIREWALL purpose to all nodes in the new default node pool(s) of a new
cluster.
Examples:

```
gcloud container clusters create example-cluster --resource-manager-tags=tagKeys/1234=tagValues/2345
gcloud container clusters create example-cluster --resource-manager-tags=my-project/key1=value1
gcloud container clusters create example-cluster --resource-manager-tags=12345/key1=value1,23456/key2=value2
gcloud container clusters create example-cluster --resource-manager-tags=
```

All nodes, including nodes that are resized or re-created, will have the
specified tags on the corresponding Instance object in the Compute Engine API.
You can reference these tags in network firewall policy rules. For instructions,
see [https://cloud.google.com/firewall/docs/use-tags-for-firewalls](https://cloud.google.com/firewall/docs/use-tags-for-firewalls).

**--security-group**:
The name of the RBAC security group for use with Google security groups in
Kubernetes RBAC (https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
To include group membership as part of the claims issued by Google during
authentication, a group must be designated as a security group by including it
as a direct member of this group.
If unspecified, no groups will be returned for use with RBAC.

**--security-posture**:
Sets the mode of the Kubernetes security posture API's off-cluster features.
To enable advanced mode explicitly set the flag to
`--security-posture=enterprise`.
To enable in standard mode explicitly set the flag to
`--security-posture=standard`
To disable in an existing cluster, explicitly set the flag to
`--security-posture=disabled`.
For more information on enablement, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement](https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement).
`SECURITY_POSTURE` must be one of: `disabled`,
`standard`, `enterprise`.

**--services-ipv4-cidr**:
Set the IP range for the services IPs.
Can be specified as a netmask size (e.g. '/20') or as in CIDR notion (e.g.
'10.100.0.0/20'). If given as a netmask size, the IP range will be chosen
automatically from the available space in the network.
If unspecified, the services CIDR range will be chosen with a default mask size.
Cannot be specified unless '--enable-ip-alias' option is also specified.

**--services-secondary-range-name**:
Set the secondary range to be used for services (e.g. ClusterIPs). NAME must be
the name of an existing secondary range in the cluster subnetwork.
Cannot be specified unless '--enable-ip-alias' option is also specified. Cannot
be used with '--create-subnetwork' option.

**--shielded-integrity-monitoring**:
Enables monitoring and attestation of the boot integrity of the instance. The
attestation is performed against the integrity policy baseline. This baseline is
initially derived from the implicitly trusted boot image when the instance is
created.

**--shielded-secure-boot**:
The instance will boot with secure boot enabled.

**--spot**:
Create nodes using spot VM instances in the new cluster.

```
gcloud container clusters create example-cluster --spot
```

New nodes, including ones created by resize or recreate, will use spot VM
instances.

**--stack-type**:
IP stack type of the node VMs. `STACK_TYPE` must be one
of: `ipv4`, `ipv4-ipv6`.

**--storage-pools**:
A list of storage pools where the cluster's boot disks will be provisioned.
STORAGE_POOL must be in the format
projects/project/zones/zone/storagePools/storagePool

**--subnetwork**:
The Google Compute Engine subnetwork
(https://cloud.google.com/compute/docs/subnetworks) to which the cluster is
connected. The subnetwork must belong to the network specified by --network.
Cannot be used with the "--create-subnetwork" option.

**--system-config-from-file**:
Path of the YAML/JSON file that contains the node configuration, including Linux
kernel parameters (sysctls) and kubelet configs.
Examples:

```
kubeletConfig:
  cpuManagerPolicy: static
  memoryManager:
    policy: Static
  topologyManager:
    policy: BestEffort
    scope: pod
linuxConfig:
  sysctl:
    net.core.somaxconn: '2048'
    net.ipv4.tcp_rmem: '4096 87380 6291456'
  hugepageConfig:
    hugepage_size2m: '1024'
    hugepage_size1g: '2'
  cgroupMode: 'CGROUP_MODE_V2'
```

List of supported kubelet configs in 'kubeletConfig'.

| KEY | VALUE |
| --- | --- |
| cpuManagerPolicy | either 'static' or 'none' |
| cpuCFSQuota | true or false (enabled by default) |
| cpuCFSQuotaPeriod | interval (e.g., '100ms') |
| memoryManager | specify memory manager policy |
| topologyManager | specify topology manager policy and scope |
| podPidsLimit | integer (The value must be greater than or equal to 1024 and less than 4194304.) |
| containerLogMaxSize | positive number plus unit suffix (e.g., '100Mi', '0.2Gi'. The value must be between 10Mi and 500Mi.) |
| containerLogMaxFiles | integer (The value must be between [2, 10].) |
| imageGcLowThresholdPercent | integer (The value must be between [10, 85], and lower than imageGcHighThresholdPercent.) |
| imageGcHighThresholdPercent | integer (The value must be between [10, 85], and greater than imageGcLowThresholdPercent.) |
| imageMinimumGcAge | interval (e.g., '100s', '1m'. The value must be less than '2m'.) |
| imageMaximumGcAge | interval (e.g., '100s', '1m'. The value must be greater than imageMinimumGcAge.) |
| allowedUnsafeSysctls | list of sysctls (Allowlisted groups: 'kernel.shm*', 'kernel.msg*', 'kernel.sem', 'fs.mqueue.*', and 'net.*', and sysctls under the groups.) |
| singleProcessOomKill | true or false |

| KEY | VALUE |
| --- | --- |
| policy | either 'Static' or 'None' |

| KEY | VALUE |
| --- | --- |
| policy | either 'none' or 'best-effort' or 'single-numa-node' or 'restricted' |
| scope | either 'pod' or 'container' |

List of supported sysctls in 'linuxConfig'.

| KEY | VALUE |
| --- | --- |
| net.core.netdev_max_backlog | Any positive integer, less than 2147483647 |
| net.core.rmem_default | Must be between [2304, 2147483647] |
| net.core.rmem_max | Must be between [2304, 2147483647] |
| net.core.wmem_default | Must be between [4608, 2147483647] |
| net.core.wmem_max | Must be between [4608, 2147483647] |
| net.core.optmem_max | Any positive integer, less than 2147483647 |
| net.core.somaxconn | Must be between [128, 2147483647] |
| net.ipv4.tcp_rmem | Any positive integer tuple |
| net.ipv4.tcp_wmem | Any positive integer tuple |
| net.ipv4.tcp_tw_reuse | Must be {0, 1, 2} |
| net.netfilter.nf_conntrack_max | Must be between [65536, 4194304] |
| net.netfilter.nf_conntrack_buckets | Must be between [65536, 524288]. Recommend setting: nf_conntrack_max = nf_conntrack_buckets * 4 |
| net.netfilter.nf_conntrack_tcp_timeout_close_wait | Must be between [60, 3600] |
| net.netfilter.nf_conntrack_tcp_timeout_time_wait | Must be between [1, 600] |
| net.netfilter.nf_conntrack_tcp_timeout_established | Must be between [600, 86400] |
| net.netfilter.nf_conntrack_acct | Must be {0, 1} |
| kernel.shmmni | Must be between [4096, 32768] |
| kernel.shmmax | Must be between [0, 18446744073692774399] |
| kernel.shmall | Must be between [0, 18446744073692774399] |
| vm.max_map_count | Must be between [65536, 2147483647] |

List of supported hugepage size in 'hugepageConfig'.

| KEY | VALUE |
| --- | --- |
| hugepage_size2m | Number of 2M huge pages, any positive integer |
| hugepage_size1g | Number of 1G huge pages, any positive integer |

Allocated hugepage size should not exceed 60% of available memory on the node.
For example, c2d-highcpu-4 has 8GB memory, total allocated hugepage of 2m and 1g
should not exceed 8GB * 0.6 = 4.8GB.
1G hugepages are only available in following machine familes: c3, m2, c2d, c3d,
h3, m3, a2, a3, g2.
Supported values for 'cgroupMode' under 'linuxConfig'.

- `CGROUP_MODE_V1`: Use cgroupv1 on the node pool.
- `CGROUP_MODE_V2`: Use cgroupv2 on the node pool.
- `CGROUP_MODE_UNSPECIFIED`: Use the default GKE cgroup configuration.

Note, updating the system configuration of an existing node pool requires
recreation of the nodes which which might cause a disruption.
Use a full or relative path to a local file containing the value of
system_config.

**--tags**:
Applies the given Compute Engine tags (comma separated) on all nodes in the new
node-pool.
Examples:

```
gcloud container clusters create example-cluster --tags=tag1,tag2
```

New nodes, including ones created by resize or recreate, will have these tags on
the Compute Engine API instance object and can be used in firewall rules. See [https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)
for examples.

**--threads-per-core**:
The number of visible threads per physical core for each node. To disable
simultaneous multithreading (SMT) set this to 1.

**--tier**:
Set the desired tier for the cluster. `TIER` must be one
of: `standard`, `enterprise`.

**--workload-metadata**:
Type of metadata server available to pods running in the node pool.
`WORKLOAD_METADATA` must be one of:

**`GCE_METADATA`**:
Pods running in this node pool have access to the node's underlying Compute
Engine Metadata Server.

**`GKE_METADATA`**:
Run the Kubernetes Engine Metadata Server on this node. The Kubernetes Engine
Metadata Server exposes a metadata API to workloads that is compatible with the
V1 Compute Metadata APIs exposed by the Compute Engine and App Engine Metadata
Servers. This feature can only be enabled if Workload Identity is enabled at the
cluster level.

**--workload-pool**:
Enable Workload Identity on the cluster.
When enabled, Kubernetes service accounts will be able to act as Cloud IAM
Service Accounts, through the provided workload pool.
Currently, the only accepted workload pool is the workload pool of the Cloud
project containing the cluster, `PROJECT_ID.svc.id.goog`.
For more information on Workload Identity, see

```
https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
```

**--workload-vulnerability-scanning**:
Sets the mode of the Kubernetes security posture API's workload vulnerability
scanning.
To enable Advanced vulnerability insights mode explicitly set the flag to
`--workload-vulnerability-scanning=enterprise`.
To enable in standard mode explicitly set the flag to
`--workload-vulnerability-scanning=standard`.
To disable in an existing cluster, explicitly set the flag to
`--workload-vulnerability-scanning=disabled`.
For more information on enablement, see [https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement](https://cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#feature-enablement).
`WORKLOAD_VULNERABILITY_SCANNING` must be one of:
`disabled`, `standard`, `enterprise`.

**--aggregation-ca**

**--binauthz-evaluation-mode**

**--cluster-dns**

**--dataplane-v2-observability-mode**

**--disable-dataplane-v2-metrics**

**--enable-autoprovisioning**

**--enable-autoscaling**

**--enable-insecure-binding-system-authenticated**:
Allow using `system:authenticated` as a subject in
ClusterRoleBindings and RoleBindings. Allowing bindings that reference
`system:authenticated` is a security risk and is not recommended.
To disallow binding `system:authenticated` in a cluster, explicitly
set the `--no-enable-insecure-binding-system-authenticated` flag
instead.

**--enable-insecure-binding-system-unauthenticated**:
Allow using `system:unauthenticated` and
`system:anonymous` as subjects in ClusterRoleBindings and
RoleBindings. Allowing bindings that reference
`system:unauthenticated` and `system:anonymous` are a
security risk and is not recommended.
To disallow binding `system:authenticated` in a cluster, explicitly
set the `--no-enable-insecure-binding-system-unauthenticated` flag
instead.

**--enable-master-authorized-networks**

**--enable-network-egress-metering**

**--enable-private-endpoint**

**--ephemeral-storage-local-ssd**

**--location**

**--maintenance-window**

**--password**

**--reservation**

**--scopes**

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

**NOTES**

: These variants are also available:

```
gcloud alpha container clusters create
```

```
gcloud beta container clusters create
```