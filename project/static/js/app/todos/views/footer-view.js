define(function (require, exports, module) {

var backbone = require('backbone');
var marionette = require('marionette');
var template = require('hbs!../templates/footer');

var ActiveCountView = require('./active-count-view').ActiveCountView;
var CompletedCountView = require('./completed-count-view').CompletedCountView;

var FooterView = marionette.Layout.extend({

    template: template,

    regions: {
        activeCount: '#todo-count',
        completedCount: '#clear-completed'
    },

    ui: {
        filters: '#filters a'
    },

    events: {
        'click #clear-completed' : 'onClearClick'
    },

    onShow: function () {
        this.activeCount.show(new ActiveCountView({ collection: this.collection }));
        this.completedCount.show(new CompletedCountView({ collection: this.collection }));
    },

    updateFilterSelection: function (filter) {
        this.ui.filters
            .removeClass('selected')
            .filter('[href="#/filter/' + filter + '"]')
            .addClass('selected');
    },

    onClearClick: function () {
        this.collection.getCompleted().forEach(function (todo) {
            todo.destroy();
        });
    }

});

exports.FooterView = FooterView;

});
