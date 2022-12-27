#!/usr/bin/env bash
PWD=`pwd`
normal(){
	sudo /home/nozaki/source/qemu-netmap/x86_64-softmmu/qemu-system-x86_64 \
		-netdev bridge,id=en0,br=virbr1 \
		-device virtio-net-pci,netdev=en0 \
		-kernel "${PWD}/build/httpreply_kvm-x86_64" \
		-append "netdev.ipv4_addr=172.44.0.2 netdev.ipv4_gw_addr=172.44.0.1 netdev.ipv4_subnet_mask=255.255.255.0 --" \
		-cpu host \
		-enable-kvm \
		--trace events=trace_list \
		-nographic
}

netmap(){
	sudo /home/nozaki/source/qemu-netmap/x86_64-softmmu/qemu-system-x86_64 \
		-netdev netmap,ifname=vale1:10,id=data1,passthrough=on \
		-device virtio-net-pci,netdev=data1 \
		-append "netdev.ipv4_addr=172.44.0.2 netdev.ipv4_gw_addr=172.44.0.1 netdev.ipv4_subnet_mask=255.255.255.0 --" \
		-kernel "${PWD}/build/httpreply_kvm-x86_64" \
		-cpu host \
		-enable-kvm \
		-nographic \
		--trace events=trace_list
}

netmap2(){
	sudo /home/nozaki/source/qemu-netmap/x86_64-softmmu/qemu-system-x86_64 \
		-netdev netmap,ifname=vale1:11,id=data1,passthrough=on \
		-device virtio-net-pci,netdev=data1 \
		-append "netdev.ipv4_addr=172.44.0.3 netdev.ipv4_gw_addr=172.44.0.1 netdev.ipv4_subnet_mask=255.255.255.0 --" \
		-kernel "${PWD}/build/httpreply_kvm-x86_64" \
		-cpu host \
		-enable-kvm \
		-nographic \
		--trace events=trace_list
}

eval "$1"
