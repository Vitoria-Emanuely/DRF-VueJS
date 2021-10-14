<template>
<v-list>
    <div class="d-flex justify-space-around flex-wrap">
      <div v-for="certificado of certificados" :key="certificado.id">
          <v-card elevation="2" outlined shaped class="mt-5 mb-5">
            <v-card-title>{{ certificado.name }}</v-card-title>
            <v-card-subtitle>Username: {{ certificado.username }}</v-card-subtitle>
            <v-card-text>Descrição: {{ certificado.description}}</v-card-text>
            <v-card-text>Grupo: {{ certificado.groups}}</v-card-text>
            <v-card-text>Expiração: {{ certificado.expiration }} dias</v-card-text>
            <v-card-text>Data de Expiração: {{ certificado.expirated_at }}</v-card-text>
            <v-card-text>Data de Criação: {{ certificado.created_at }}</v-card-text>
            <v-card-text>Data de Atualização: {{ certificado.updated_at }}</v-card-text>
            <v-card-actions class="justify-center"><certificado-edit :id="certificado.id" :name="certificado.name" :username="certificado.username" :description="certificado.description"
            :groups="certificado.groups[0].toString()" :expiration="certificado.expiration" :expirated_at="certificado.expirated_at"
            :created_at="certificado.created_at" :updated_at="certificado.updated_at"/>
            <v-btn text color="red accent-4"  @click="delCertificate(certificado.id)">Excluir</v-btn></v-card-actions>
        </v-card>

      </div>
    </div>
    </v-list>
</template>

<script>

import CertificadoEdit from '@/components/CertificadoEdit.vue'
import axios from 'axios'

export default {
    components: { CertificadoEdit },
    data(){
        return {
            certificados: [],
        }
    },  
    mounted() {
        this.getCertificate()
        this.$root.$refs.CertificadoView = this
    },
    methods: {
        getCertificate(){
            axios.get('http://localhost:8000/').then(response => {
            this.certificados = response.data
            }).catch((error) => {
                console.log(error);
            });
        }, 
        delCertificate(id){
            axios.delete(`http://localhost:8000/${id}`).then(() => {
            console.log('Deletado com sucesso')
            this.getCertificate()
            }).catch((error) => {
                console.log(error);
            });
        }
    }
}
</script>

<style>
</style>