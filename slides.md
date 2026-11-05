---
marp: true
theme: flatcar
paginate: false
size: 16:9
title: "Flatcar Container Linux: KubeCon NA 2026 Booth Loop"
author: Flatcar Maintainers
---

<style>
/* Booth screens are read from a few meters away: bigger type, bigger gaps. */
section.booth ul li { font-size: 36px; line-height: 1.25; margin-bottom: 16px; }
section.booth h1 { font-size: 58px; }
section.booth > p { margin-top: 30px; font-size: 34px; text-align: center; font-weight: 700; }
section.booth .cncf-banner { margin-top: 30px; }
section.booth.centered { justify-content: center; padding-top: 178px; }
section.booth .cncf-banner img { max-height: 90px; width: auto; margin: 0 auto; }
section.qrs { padding: 50px 70px; justify-content: center; }
section.qrs .qr-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 28px; width: 100%; margin-top: 24px; }
section.qrs .qr-card { background: #fff; border-radius: 14px; padding: 14px 14px 18px; text-align: center; }
section.qrs .qr-card img { display: block; width: 100%; height: auto; }
section.qrs .qr-card p { margin: 0; color: #12172B; font-size: 28px; font-weight: 700; line-height: 1.15; }
section.qrs .qr-card p span { display: block; font-size: 20px; font-weight: 400; margin-top: 4px; }
section.qrs p.where { margin: 28px 0 0 0; font-size: 28px; color: #fff; }
section.qrs .qr-head { display: flex; align-items: center; gap: 28px; }
section.qrs .qr-head img { height: 100px; width: auto; }
section.qrs .qr-head h1 { font-size: 56px; margin: 0; }
section.qrs .qr-head h2 { font-size: 28px; margin: 6px 0 0 0; }
section.qrs .qr-row { margin-top: 28px; }
section.qrs p.where { margin: 22px 0 8px 0; }
section.qrs p.meetings { display: flex; gap: 40px; margin: 0; font-size: 22px; color: #fff; }
section.qrs p.meetings strong { color: #09BAC8; }
section.booth-title { padding: 70px 100px 60px; }
section.booth-title h1 { background-size: 150px auto; padding: 190px 0 0 0; font-size: 84px; max-width: 100%; white-space: nowrap; }
section.booth-title h2 { font-size: 42px; margin: 20px 0 auto 0; max-width: 100%; }
section.booth-title p.event { font-size: 34px; font-weight: 700; color: #09BAC8; padding-bottom: 10px; }
section.booth-title p.where { font-size: 28px; padding-bottom: 0; }
section.qrs p.where { font-size: 30px !important; }
section.qrs p.meetings { font-size: 26px !important; }
section.designed {
  background-image: url('assets/backgrounds/flatcar-staircase-right.svg');
  background-repeat: no-repeat;
  background-position: right -60px bottom -588px;
  background-size: 75% auto;
  padding: 64px 70px;
  justify-content: flex-start;
  align-items: stretch;
}
section.designed p.kicker { margin: 0 0 10px 0; display: inline-flex; align-items: center; gap: 12px; color: #09BAC8; font-size: 22px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; }
section.designed h1 { margin: 0 0 40px 0; padding: 0; color: #fff; font-size: 56px; font-weight: 700; line-height: 1.1; }
section.designed .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
section.designed .card { padding: 28px 28px 32px; border-left: 4px solid #09BAC8; border-radius: 0 6px 6px 0; background: #1E2540; box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35); }
section.designed .card p.num { margin: 0 0 8px 0; color: #09BAC8; font-size: 20px; font-weight: 700; letter-spacing: 0.14em; }
section.designed .card p.title { margin: 0 0 14px 0; color: #fff; font-size: 40px; font-weight: 700; line-height: 1.15; min-height: 92px; }
section.designed .card p.sub { margin: 0; color: #C9CEDD; font-size: 26px; line-height: 1.35; }
</style>

<!-- _class: cover booth-title -->
<!-- _paginate: false -->

# Flatcar Container Linux

## A secure, minimal Linux for containers

<p class="event">KubeCon + CloudNativeCon North America 2026</p>
<p class="where"><strong>Project Pavilion, kiosk P-8A</strong> · Hall 5, Cosmic Canyon Zone</p>

---

<!-- _class: booth centered -->

# A secure, minimal Linux for containers

- **Purpose-built for containers:** no package manager, no config drift
- **Immutable filesystem:** eliminates entire classes of vulnerabilities
- **Atomic A/B updates:** reliable, always-current OS upgrades
- **Ignition provisioning:** declarative setup on first boot
- **Open and vendor-neutral:** stewarded by the CNCF

<div class="cncf-banner">
  <img src="assets/logos/external/cncf-banner.png" alt="Cloud Native Computing Foundation">
</div>

---

<!-- _class: lead designed -->

<p class="kicker">Flatcar Container Linux</p>

# Designed for

<div class="cards">
  <div class="card">
    <p class="num">01</p>
    <p class="title">Containers</p>
    <p class="sub">Kubernetes or your runtime of choice</p>
  </div>
  <div class="card">
    <p class="num">02</p>
    <p class="title">Infra automation</p>
    <p class="sub">Declarative provisioning with Ignition</p>
  </div>
  <div class="card">
    <p class="num">03</p>
    <p class="title">Security</p>
    <p class="sub">Read-only, verified, automatically updated</p>
  </div>
</div>

---

<!-- _class: booth -->

# Runs everywhere

<div class="logo-wall" style="grid-template-columns: repeat(5, 1fr); grid-template-rows: repeat(2, 1fr); gap: 30px 36px; height: 380px; margin-top: 20px">
  <img src="assets/logos/external/clouds/aws-logo.svg" alt="AWS">
  <img src="assets/logos/external/clouds/azure.svg" alt="Azure">
  <img src="assets/logos/external/clouds/gcp.png" alt="GCP">
  <img src="assets/logos/external/clouds/openstack.png" alt="OpenStack">
  <img src="assets/logos/external/clouds/hetzner.png" alt="Hetzner">
  <img src="assets/logos/external/clouds/Vmware.svg" alt="VMware">
  <img src="assets/logos/external/clouds/Logo_Proxmox.svg" alt="Proxmox">
  <img src="assets/logos/external/clouds/Qemu_logo.svg" alt="QEMU">
  <img src="assets/logos/external/clouds/kube-virt.svg" alt="KubeVirt">
  <img src="assets/logos/external/clouds/akamai-logo.svg" alt="Akamai">
</div>

Plus bare metal, and many more.

---

<!-- _class: lead qrs -->
<!-- _paginate: false -->

<div class="qr-head">
  <img src="assets/logos/flatcar-logotype/icon/color/flatcar-icon-color.svg" alt="Flatcar">
  <div>
    <h1>Come talk to us</h1>
    <h2>Scan a code to find the community, the code and the docs</h2>
  </div>
</div>

<div class="qr-row">
  <div class="qr-card"><img src="assets/qr/flatcar_org.png" alt="flatcar.org"><p>Website<span>flatcar.org</span></p></div>
  <div class="qr-card"><img src="assets/qr/flatcar_gh.png" alt="GitHub"><p>GitHub<span>flatcar/Flatcar</span></p></div>
  <div class="qr-card"><img src="assets/qr/flatcar_discord.png" alt="Discord"><p>Discord<span>Chat with the community</span></p></div>
  <div class="qr-card"><img src="assets/qr/flatcar_learning_series.png" alt="Learning series"><p>Learning series<span>Get started with Flatcar</span></p></div>
</div>

<p class="where"><strong>Find us at the Project Pavilion, kiosk P-8A</strong> · Hall 5, Cosmic Canyon Zone</p>

<p class="meetings">
  <span><strong>Office hours</strong> · every 2nd Thu, 16:30 CEST</span>
  <span><strong>Dev sync</strong> · every 4th Thu, 16:30 CEST</span>
</p>
