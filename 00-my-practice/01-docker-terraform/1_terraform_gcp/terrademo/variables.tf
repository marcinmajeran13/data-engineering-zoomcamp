variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "location" {
  description = "Project Location"
  default     = "us-west1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "Bucket Storage Name"
  default     = "mmajer-terraform-bucket"
}

variable "region" {
  description = "Project's Region"
  default     = "us-west1"
}

variable "project_id" {
  default = "capable-blend-427212-e6"
}


