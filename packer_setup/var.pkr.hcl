variable "project_id" {
  type = string
}
variable "source_image_family" {
  type = string
}
variable "image_name" {
  type = string
}
variable "zone" {
  type = string
}
variable "ssh_username" {
  type = string
}
variable "dev_deploy_image_name" {
  default = "centos-dev-deploy"
}
variable "network" {
  type = string
}
