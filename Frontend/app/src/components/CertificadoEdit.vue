<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="850">
      <template v-slot:activator="{ on, attrs }">
        <v-btn text color="teal accent-4" v-bind="attrs" v-on="on">Editar</v-btn>
      </template>
      <v-card>
        <v-card-title class="text-h5 teal lighten-1 white--text justify-center">Editar Informações</v-card-title>
        <v-card-text>
          <v-form ref="form" class="pt-7"> 
            <v-row justify="center"><v-col cols="4"><v-text-field label="Nome" v-model="currentName" :rules="inputRules" required></v-text-field></v-col>
            <v-col cols="4"><v-text-field label="Usuário" v-model="currentUsername" :rules="inputRules" required></v-text-field></v-col></v-row>
            <v-row justify="center">
              <v-col cols="8"><v-text-field label="Descrição" v-model="currentDescription"></v-text-field></v-col>
            </v-row>
            <v-row justify="center"><v-col cols="4"><v-select class="select" label="Grupo" v-model="currentGroups" :rules="inputRules" :items="groupsC" required></v-select></v-col></v-row>
          </v-form>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="teal accent-4" @click="putCertificate(id)">Salvar</v-btn>
          <v-btn color="accent-4 red" text @click="dialog = false">Cancelar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: { id: Number, name: String, username: String, description: String, groups: String, expiration: Number,
  expirated_at: String, created_at: String, updated_at: String},
  data() {
    return {
      dialog: false,  
      groupsC: [
        {text: "Adm (01)", value: '1'},
        {text: "Comercial (15)", value: '15'},
        {text: "RH (30)", value: '30'},
      ],
      currentName: this.name,
      currentUsername: this.username,
      currentDescription: this.description,
      currentGroups: this.groups,
      currentExpiration: this.expiration,
      currentExpirated: this.expirated_at,
      currentCreated: this.created_at,
      currentUpdated: this.updated_at,
      inputRules: [
        v => !!v || 'Campo obrigatório',
      ],
    }
  },
  methods: {
    putCertificate(id){
      axios.put(`http://localhost:8000/${id}`, {username: this.currentUsername, name: this.currentName, description: this.currentDescription,
      groups: [this.currentGroups], expiration: this.currentExpiration, expirated_at: this.currentExpirated, created_at: this.currentCreated, updated_at: this.$root.$refs.CertificadoForm.getDate()}).then(() => {
        this.$root.$refs.CertificadoView.getCertificate()
        console.log('Editado com sucesso')
        }).catch((error) => {
          console.log(error.response);
      });
    }
  } 
}
</script>