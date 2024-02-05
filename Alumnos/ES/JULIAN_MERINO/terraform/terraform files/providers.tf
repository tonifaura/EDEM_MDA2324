provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

terraform {
  backend "gcs" {
    bucket = "jumepre-terraform-project"
    prefix = "terraform/state"
  }
}