## Spark Operator & PySpark Job Deployment Guide (Kubeflow)

### Prerequisites
* Kubeflow namespace available (`kubeflow`)
* Spark Operator installed and running
    cmd: kubectl get pods -n kubeflow | grep spark-operator
* Service account `spark` created with proper permissions
   cmd: kubectl create serviceaccount spark -n kubeflow
   cmd: kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=kubeflow:spark --namespace=kubeflow

### Create ConfigMap (for PySpark script if custom)
If using a custom PySpark file (like pi.py):
  create cmd: kubectl create configmap pyspark-job --from-file=pyspark-job.py -n kubeflow
  verify cmd: kubectl get configmap pyspark-job -n kubeflow

### Deploy Spark Job**
Apply the SparkApplication YAML (example: spark-python-test-pi.yaml):
  cmd: kubectl apply -f spark-pi-github.yaml -n kubeflow

### Check Application Status**
CMD: kubectl get sparkapplications -n kubeflow
Check detailed status:
  CMD: kubectl describe sparkapplication spark-pi-github -n kubeflow

### Monitor Pods
  CMD: kubectl get pods -n kubeflow -w | grep spark-pi-github

### Check Driver Logs for Output
CMD: kubectl logs <driver-pod-name> -n kubeflow

You should see PI output like: 'Pi is roughly 3.1423'

###Cleanup
kubectl delete -f spark-pi-github.yaml -n kubeflow

### Summary
* Spark Operator and SparkApplication tested successfully
* Job executed in cluster mode with driver & executor pods
* Verified PI output and applied security contexts
