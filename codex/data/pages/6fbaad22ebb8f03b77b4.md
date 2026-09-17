---
url: https://cortex-docs.paloaltonetworks.com/appsec-rules/iac-security/networking/appsec-k8s-154
fetched_at: 2026-09-16T09:09:33Z
source: cortex-platform
---

# NGINX Ingress has annotation snippets which contain alias statements misconfiguration detected in co | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Alerts & Rules 

 AppSec Rules 

 IaC Security 

 Networking 

 NGINX Ingress has annotation snippets which contain alias statements misconfiguration detected in co 

 Rule Details 

 Cortex AppSec Rule ID 

 APPSEC_K8S_154 

 Category - Subcategory 

 Kubernetes - Native Security Controls 

 Provider 

 OTHER 

 Severity 

 LOW 

 Framework 

 Helm, Kubernetes, Kustomize 

 Impact 

 Allowing custom snippet annotations in ingress-nginx enables a user, who can create or update ingress objects, to obtain all secrets in the cluster. To still allow users leveraging the snippet feature it is recommend to remove any usage of alias. Learn more around https://nvd.nist.gov/vuln/detail/CVE-2021-25742[CVE-2021-25742] 

 How to Fix 

 [source,go] 

 { "apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: example-ingress namespace: developer annotations: kubernetes.io/ingress.class: nginx nginx.ingress.kubernetes.io/rewrite-target: /$2 nginx.ingress.kubernetes.io/server-snippet: | location ^~ "/test" { default_type 'text/plain'; 

 alias /var/run; } 

 spec: rules: 

 http: paths: 

 path: /test pathType: Prefix backend: service: name: web port: number: 8080", } 

 Previous NGINX Ingress has annotation snippets misconfiguration detected in code 

 Next OCI Network Security Groups (NSG) has stateful security rules misconfiguration detected in code 

 Last updated 1 month ago 

 Was this helpful?
