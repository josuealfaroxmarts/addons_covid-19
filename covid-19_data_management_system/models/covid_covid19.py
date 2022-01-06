# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Covid19(models.Model):
    _name = 'covid.covid19'
    _description = 'COVID-19'

    source = fields.Char(string="Fuente", required=True)
    datetime = fields.Datetime(string="Fecha y hora", required=True, default=fields.Datetime.now())
    country_id = fields.Many2one('res.country', required=True)
    infected = fields.Integer(string="Infectados", required=True, default=0)
    recovered = fields.Integer(string="Recuperados", required=True, default=0)
    deceased = fields.Integer(string="Fallecidos", required=True, default=0)

    total_infected = fields.Integer(string="Total infectados", compute="_compute_get_total_infected", 
            store=True, required=True, default=0)
    total_recovered = fields.Integer(string="Total recuperados", compute="_compute_get_total_recovered", 
            store=True, required=True, default=0)
    total_deceased = fields.Integer(string="Total fallecidos", compute="_compute_get_total_deceased", 
            store=True, required=True, default=0)

    @api.depends('infected')
    def _compute_get_total_infected(self):
        """Método que obtiene el valor total de personas infectadas por país"""
        for data in self:
            records = self.search(
                [
                    # valor del país del registro actual coincida con valor del país de los registros reccorridos
                    ('country_id', '=', data.country_id.id),
                    ('datetime', '<', data.datetime)
                ]
            )
            infected_vals = records.mapped('infected')
            data.total_infected = data.infected + sum(infected_vals) 

    @api.depends('recovered')
    def _compute_get_total_recovered(self):
        """Método que obtiene el valor total de personas recuperadas por país"""
        for data in self:
            records = self.search(
                [
                    ('country_id', '=', data.country_id.id), 
                    ('datetime', '<', data.datetime)
                ]
            )
            recovered_vals = records.mapped('recovered')
            data.total_recovered = data.recovered + sum(recovered_vals) 

    @api.depends('deceased')
    def _compute_get_total_deceased(self):
        """Método que obtiene el valor total de personas fallecidas por país"""
        for data in self:
            records = self.search(
                [
                    ('country_id', '=', data.country_id.id), 
                    ('datetime', '<', data.datetime)
                ]
            )
            deceased_vals = records.mapped('deceased')
            data.total_deceased = data.deceased + sum(deceased_vals) 