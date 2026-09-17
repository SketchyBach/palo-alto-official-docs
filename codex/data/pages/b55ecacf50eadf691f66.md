---
url: https://docs.prismacloud.io/content-collections/administration/network-security/container-network-exposure/customize-satellite-deployment
fetched_at: 2026-09-16T13:35:09Z
source: prisma-cloud
---

# Customize Satellite Deployment | Prisma Cloud arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Enterprise Edition 

 Content Collections 

 Administration 

 Network Security 

 Container Network Exposure 

 Customize Satellite Deployment 

 You can use a Secret Manager to store Satellite information and customize your Satellite deployment: 

 Use Kubernetes Secrets (default option) or third-party Secrets Managers and mount it as a dot file into the deployment as volume. 

 Ask Copy 

 apiVersion: v1 
 kind: Secret 
 metadata: 
 name: prismacloud-satellite-secret 
 labels: 
 {{- include "prismacloud-satellite.labels" . | nindent 4 }} 
 type: Opaque 
 data: 
 .PRISMA_API_SECRET: {{ .Values.global.satellite.accessKey | b64enc }} 
 .PROXY_PASSWORD: {{ .Values.global.proxy.password | quote | b64enc }} 
 .PROXY_USER: {{ .Values.global.proxy.user | quote | b64enc }} 

 apiVersion: v1 
 kind: Pod 
 metadata: 
 name: secret-dotfiles-pod 
 spec: 
 volumes: 
 - name: prisma-api-secret 
 secret: 
 secretName: prismacloud-satellite-secret 
 containers: 
 - name: test-container 
 image: registry.k8s.io/busybox 
 command: 
 - ls 
 - "-l" 
 - "/etc/secret-volume" 
 volumeMounts: 
 - name: prisma-api-secret 
 readOnly: true 
 mountPath: "/etc/secrets" 

 Use the GCP CSI driver secrets add on, which mounts the GCP managed secrets as volume. 

 Define which secrets to mount, create a SecretProviderClass yaml manifest, and list the secrets to mount and the filename to mount them as. 

 Ask Copy 

 apiVersion: secrets-store.csi.x-k8s.io/v1 
 kind: SecretProviderClass 
 metadata: 
 name: gke-secrets 
 spec: 
 provider: gke 
 parameters: 
 secrets: | 
 - resourceName: "projects/<your-project-id>/secrets/<my-api-token>/versions/latest" 
 path: "<secret-filename>" 

 apiVersion: v1 
 kind: Pod 
 metadata: 
 name: secret-dotfiles-pod 
 spec: 
 volumes: 
 - name: prisma-api-secret 
 csi: 
 driver: secrets-store.csi.k8s.io 
 readOnly: true 
 volumeAttributes: 
 secretProviderClass: "gke-secrets" 
 containers: 
 - name: test-container 
 image: registry.k8s.io/busybox 
 command: 
 - ls 
 - "-l" 
 - "/etc/secret-volume" 
 volumeMounts: 
 - name: prisma-api-secret 
 readOnly: true 
 mountPath: "/etc/secrets" 

 Previous Troubleshoot Container Network Exposure Issues 

 Next Alarm Center 

 Last updated 3 months ago 

 Was this helpful?
