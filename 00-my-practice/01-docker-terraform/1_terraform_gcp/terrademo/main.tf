terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.1.0"
    }
  }
}

provider "google" {
  credentials = "./keys/my-creds.json"
  project     = "capable-blend-427212-e6"
  region      = "us-west1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "mmajer-terraform-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
