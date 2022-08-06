<<<<<<< HEAD
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
=======
>>>>>>> e6b54fb (asdu)
  transpileDependencies: [
    'quasar'
  ],

  pluginOptions: {
    quasar: {
      importStrategy: 'kebab',
      rtlSupport: false
    }
  }
<<<<<<< HEAD
<<<<<<< HEAD
=======
  transpileDependencies: true
>>>>>>> 1f63946 (vue 환경셋팅)
=======
>>>>>>> 34b83a2 (Feat : 퀘이사 UI Framework 적용)
=======
>>>>>>> e6b54fb (asdu)
})
=======
const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["quasar"],

  pluginOptions: {
    quasar: {
      importStrategy: "kebab",
      rtlSupport: false,
    },
  },
});
>>>>>>> ffe7e28 (백 프론트 파일 복사했어유)
