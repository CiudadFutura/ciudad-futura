'use strict'

var gulp = require('gulp'),
    less = require('gulp-less'),
    path = require('path'),
    fs = require('fs'),
    helpers = require('./lib/gulp-helpers');

var APPS_PATH = 'src/ciudadfutura/apps'
var APPS = fs.readdirSync(APPS_PATH).filter(function(path) {
    return path.indexOf('__init__') === -1;
})

var logger = new helpers.Logger({
    gulp: gulp,
    defaultTask: 'watcher'
});

gulp.task('less', function () {
    APPS.forEach(function(app) {
        var path = 'src/ciudadfutura/apps/' + app + '/static/' + app;

        if (!helpers.pathExists(path + '/less')) {
            return logger.warning('Empty static for app: ' + app);
        }

        logger.success('Compiling static for app: ' + app);
        gulp.src(path + '/less/**/*.less')
            .pipe(less().on('error', function (event) {
                logger.error('Error while compiling static for app: ' + app);
                logger.error(event.message);
            }))
            .pipe(gulp.dest(path + '/css'));
    });
});

gulp.task('dev', ['less'], function () {
    gulp.watch(APPS_PATH + '/**/static/**/*.less', ['less'])
        .on('change', function(event) {
            logger.info('(' + event.type + ') ' + event.path.split(APPS_PATH).pop())
        });
})

gulp.task('default', ['dev'])
