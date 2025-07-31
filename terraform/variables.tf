variable "project_id" {
  description = "Your GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Unique bucket name"
  type        = string
}

variable "credentials_file" {
  description = "Path to your service account key"
  type        = string
}
