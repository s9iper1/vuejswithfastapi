<template>
  <div class="moviestar">
    <h1>80s Movie Stars</h1>

    <br>
    <button @click="fetch_stars()">Click to fetch</button>
    <br><br>

    <div align="center" v-if="moviestars">
      <table>
        <tr>
          <th>Name</th>
          <th>Movies</th>
        </tr>
        <tr v-for="(star, name) in moviestars" :key="name">
          <td>{{name}}</td>
          <td><li v-for="movie in star.movies" :key="movie">{{movie}}</li></td>
        </tr>
      </table>
    </div>

    <br>

    <button v-if="moviestars" @click="moviestars=null">Clear</button>


  </div>
</template>

<script>
export default {
  name: 'MovieStar',
  data() {
    return {
      moviestars: '',
      vue_env: process.env.VUE_APP_ENV,
    }
  },
  methods : {
    // fetch movie stars from python API
    fetch_stars() {
      fetch("http://localhost:3000/fetch", {
        mode: 'no-cors',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        }
      }).then(async response => {
        try {
          console.log(response.status)
          let apidata = await response.json();
          console.log(apidata);
          this.moviestars = apidata;
          this.errorMessage = false;
        } catch (err) {
          // 👇️ SyntaxError: Unexpected end of JSON input
          console.log('error', err);
        }
      }).catch(error => {
            this.errorMessage = error;
            console.log(error)
            // console.error(error);
          });
    },
  }
}
</script>

<style>
table, th, td { border: 1px solid black; padding:5px }
</style>