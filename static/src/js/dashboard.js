/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component, useState} from "@odoo/owl";
import {loadJS} from "@web/core/assets";

const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.state = useState({
            selecteddate: false,
        })
        this._fetch_data();

    }

    async _fetch_data() {
        if (this.state.selecteddate == false) {
            var result = await this.orm.call("crm.lead", "get_tiles_data", [], {'date': false});
        } else {
            var result = await this.orm.call("crm.lead", "get_tiles_data", [], {'date': this.state.selecteddate});
        }

        document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
        document.getElementById('win_ratio').innerHTML = `<span>${result.win_ratio}</span>`;
        document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
        document.getElementById('expected_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
        document.getElementById('total_revenue').innerHTML = `<span>${result.currency}${result.revenue}</span>`;
        await loadJS(["/web/static/lib/Chart/Chart.js"])

        var chart = new Chart("all_tile_chart", {
            type: "bar",
            data: {
                labels: [result.total_leads_label, result.win_ratio_label, result.total_opportunity_label, result.expected_revenue_label, result.revenue_label],
                datasets: [{
                    data: [result.total_leads, result.win_ratio_int, result.total_opportunity, result.expected_revenue, result.revenue],
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });

        var chart = new Chart("activity_pie_chart", {
            type: "pie",
            data: {
                labels: result.activity_labels,
                datasets: [{
                    data: result.activity_values,
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });

        var chart = new Chart("lost_lead_graph", {
            type: "doughnut",
            data: {
                labels: result.lost_leads_labels,
                datasets: [{
                    label: 'Lost Lead Graph',
                    data: result.lost_leads_values,
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });

        var chart = new Chart("campaign_lead_graph", {
            type: "line",
            data: {
                labels: result.campaign_leads_labels,
                datasets: [{
                    label: 'Campaign',
                    data: result.campaign_leads_values,
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });


        var chart = new Chart("medium_lead_graph", {
            type: "scatter",
            data: {
                labels: result.medium_labels,
                datasets: [{
                    label: 'Medium Lead Graph',
                    data: [{
                        x: result.medium_values[0],
                        y: result.medium_values[0]
                    }, {
                        x: result.medium_values[1],
                        y: result.medium_values[1]
                    }, {
                        x: result.medium_values[2],
                        y: result.medium_values[2]
                    }, {
                        x: result.medium_values[3],
                        y: result.medium_values[3]
                    }, {
                        x: result.medium_values[4],
                        y: result.medium_values[4]
                    }],
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });

    }

}

CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
