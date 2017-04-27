module.exports = function(grunt) {

  grunt.initConfig({
    jshint: {
      files: ['Gruntfile.js', 'src/**/*.js', 'test/**/*.js'],
      options: {
        globals: {
          jQuery: true
        }
      }
    },
    copy: {
      main: {
        files: [
          {expand: true, cwd: 'node_modules/bootstrap/dist', src: ['**'], dest: 'aplicacionTurnos/static/vendor/bootstrap', filter: 'isFile'},
          {expand: true, cwd: 'node_modules/jquery/dist', src: ['**'], dest: 'aplicacionTurnos/static/vendor/jquery', filter: 'isFile'},
          {expand: true, cwd: 'node_modules/bootstrap-datepicker/dist', src: ['**'], dest: 'aplicacionTurnos/static/vendor/bootstrap-datepicker', filter: 'isFile'},
          {expand: true, cwd: 'node_modules/datepair/dist', src: ['**'], dest: 'aplicacionTurnos/static/vendor/datepair', filter: 'isFile'},
          {expand: true, cwd: 'node_modules/font-awesome/css', src: ['**'], dest: 'aplicacionTurnos/static/vendor/font-awesome/css', filter: 'isFile'},
          {expand: true, cwd: 'node_modules/font-awesome/fonts', src: ['**'], dest: 'aplicacionTurnos/static/vendor/font-awesome/fonts', filter: 'isFile'}
        ],
      },
    },
    browserify: {
      main: {
          src: 'aplicacionTurnos/static/js/turnos.js',
          dest: 'aplicacionTurnos/static/bundle.js'
      }
    },
    less: {
        options: {
            sourceMap: true
        },
        dist: {
            files: {
                'aplicacionTurnos/static/css/main.css': 'aplicacionTurnos/resources/less/main.less'
            }
        }
    },
    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    }
  });

  /*grunt.loadNpmTasks('grunt-contrib-jshint');*/
  /*grunt.loadNpmTasks('grunt-contrib-watch');*/
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-contrib-less');

  grunt.registerTask('default', ['copy', 'browserify', 'less']);

};
