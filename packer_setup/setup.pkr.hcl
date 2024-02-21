source "googlecompute" "centos-csye" {
  project_id          = var.project_id
  source_image_family = var.source_image_family
  image_name          = var.image_name
  image_description   = "A custom CentOS Stream 8 image with Python installed"
  ssh_username        = var.ssh_username
  zone                = var.zone
  network             = var.network
}

build {
  sources = ["sources.googlecompute.centos-csye"]

  provisioner "shell" {
    scripts = [
      "./packer_setup/setup_db.sh",
    ]
  }
}
