var gulp = require('gulp'),
    less = require('gulp-less'),
    util = require('gulp-util'),
    colors = util.colors;


gulp.task('less', function () {
    gulp.src('src/ciudadfutura/apps/site/static/site/less/**/*.less')
        .pipe(less().on('error', function (event) {
            util.log(colors.cyan('Error while compiling less...'));
            util.log(colors.red(event.message));
        }))
        .pipe(gulp.dest('src/ciudadfutura/apps/site/static/site/css'));
});


gulp.task('dev', ['less'], function () {

    gulp.watch('src/ciudadfutura/apps/**/static/**/*.less', ['less'])
        .on('change', function(event) {
            util.log(colors.yellow('[less:' + event.type + '] ' + event.path));
        });

    gulp.watch(['src/!(bundle).js', 'src/js/**/*.js'], ['bundle'])
        .on('change', function(event) {
            util.log(colors.yellow('[js:' + event.type + '] ' + event.path));
        });
});
