var util = require('gulp-util'),
    colors = util.colors,
    fs = require('fs');

function Logger(options) {

    var defaultTask = options.defaultTask || 'watcher';
    var currentTask;

    options.gulp.on('task_start', function(event) {
        currentTask = event.task;
    });

    options.gulp.on('task_stop', function(event) {
        currentTask = undefined;
    });

    this.log = function(color, message) {
        var task = currentTask || defaultTask;
        util.log(color('[' + task + '] ' + message));
    };
}
Logger.prototype.success = function(message) {
    this.log(colors.green, message);
};
Logger.prototype.error = function(message) {
    this.log(colors.red, message);
};
Logger.prototype.warning = function(message) {
    this.log(colors.yellow, message);
};
Logger.prototype.info = function(message) {
    this.log(colors.cyan, message);
};

var pathExists = function(path) {
    try {
        fs.accessSync(path);
        return true;
    } catch(e) {}
    return false;
};

module.exports = {
    Logger: Logger,
    pathExists: pathExists,
}
