<template>
  <v-form ref="form">
    <v-row class="pt-4 pb-4">   
      <v-col cols="2"><v-text-field label="Nome" v-model="certificado.name" :rules="inputRules" required></v-text-field></v-col>
      <v-col cols="2"><v-text-field label="Usuário" v-model="certificado.username" :rules="inputRules" required></v-text-field></v-col>
      <v-col cols="4"><v-text-field label="Descrição" v-model="certificado.description"></v-text-field></v-col>
      <v-col cols="1"><v-select class="select" label="Grupo" v-model="certificado.groups" :rules="inputRules" :items="groups" required></v-select></v-col>      
      <v-col cols="2"><v-text-field label="Dias de Expiração" v-model="certificado.expiration" :rules="inputRules" type="number" required></v-text-field></v-col>
      <v-icon slot="append" @click="postCertificate">mdi-send</v-icon>
    </v-row>
  </v-form>
</template>

<script>
import axios from 'axios'
import moment from 'moment'

export default {
  data() {
    return {
      certificado: {
        username: "",
        name: "",
        description: "",
        groups: "",
        expiration: "",
      },
        groups: [
        {text: "Adm (01)", value: '1'},
        {text: "Comercial (15)", value: '15'},
        {text: "RH (30)", value: '30'},
      ],
      inputRules: [
        v => !!v || 'Campo obrigatório',
      ],
    }
  },
  mounted() {
    this.$root.$refs.CertificadoForm = this
  },
  methods: {
      getDate(){
          var today = new Date();
          var datetime = moment(today).format()
          return datetime
      },
      getExpirated(expiration){
          var today = new Date();
          var expirated = today.setDate(today.getDate() + parseInt(expiration))
          var res = moment(expirated).format()
          return res
      },
    postCertificate() {
        axios.post('http://localhost:8000/', {username: this.certificado.name, name: this.certificado.name, description: this.certificado.description,
        groups: [this.certificado.groups], expiration: this.certificado.expiration, expirated_at: this.getExpirated(this.certificado.expiration), created_at: this.getDate(), updated_at: this.getDate()}).then(() => {
            console.log('Cadastrado com sucesso')
            this.certificado.username = ""
            this.certificado.name = ""
            this.certificado.description = ""
            this.certificado.groups = ""
            this.certificado.expiration = ""
            this.$refs.form.resetValidation()
            this.$root.$refs.CertificadoView.getCertificate()
        }).catch((error) => { console.log(error.response);
        });    
        
      }  
    },
}
</script>

<style>
</style>