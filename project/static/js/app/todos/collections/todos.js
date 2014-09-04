define(function (require, exports, module) {

var backbone = require('backbone');
var marionette = require('marionette');
var Todo = require('../models/todo').Todo;

var Todos  =  backbone.Collection.extend({
    model: Todo,

    meta: {},

    url: "/api/v1/todo",

    getCompleted: function () {
      return this.where({completed: true});
    },

    getActive: function () {
      return this.where({completed: false});
    },

    parse: function(response) {
        this.meta = response.meta;
        return response.objects;
    },

    comparator: 'created'
});

exports.Todos = Todos;

});
