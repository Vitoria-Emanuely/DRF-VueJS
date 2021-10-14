<template>
  <v-container class="pa-8" fluid>
    <h1 class="h1">{{ titulo }}</h1>    
    <certificado-form />
    <v-divider class="pt-5"></v-divider>
    <certificado-view  />
  </v-container>
</template>

<script>
import CertificadoForm from '@/components/CertificadoForm.vue'
import CertificadoView from '@/components/CertificadoView.vue'

export default {
  components: { CertificadoForm, CertificadoView },
  data() {
    return {
      titulo: "Certificados",
    }
  },
}
</script>

<style>
</style>