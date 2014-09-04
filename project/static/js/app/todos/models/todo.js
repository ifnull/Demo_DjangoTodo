define(function( require, exports, module ){

var backbone = require('backbone');

var Todo = backbone.Model.extend({

    defaults: {
        title: '',
        completed: false,
        created: null
    },

    url: function() {
        var id = this.id || '';
        return "/api/v1/todo/"+id;
    },

    toggle: function () {
        return this.save('completed', !this.get('completed'), {patch: true});
    }
});

exports.Todo = Todo;

});
