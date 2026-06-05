/** @odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component} from "@odoo/owl";
import { loadJS } from "@web/core/assets";

const actionRegistry = registry.category("actions");

class CrmDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this._fetch_data();
    }

    async _fetch_data() {
        let result = await this.orm.call("crm.lead", "get_tiles_data", [], {});
        document.getElementById('my_lead').innerHTML = `<span>${result.total_leads}</span>`;
        document.getElementById('win_ratio').innerHTML = `<span>${result.win_ratio}</span>`;
        document.getElementById('my_opportunity').innerHTML = `<span>${result.total_opportunity}</span>`;
        document.getElementById('expected_revenue').innerHTML = `<span>${result.currency}${result.expected_revenue}</span>`;
        document.getElementById('total_revenue').innerHTML = `<span>${result.currency}${result.revenue}</span>`;
        await loadJS(["/web/static/lib/Chart/Chart.js"])

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
            type: "bar",
            data: {
                labels: result.lost_leads_labels,
                datasets: [{
                    label:'Lost Lead Graph',
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
                    label:'Campaign Lead Graph',
                    data: result.campaign_leads_values,
                    pointBackgroundColor: "black",
                }]
            },
            option: {}
        });

    }

}

CrmDashboard.template = "crm_dashboard.CrmDashboard";
actionRegistry.add("crm_dashboard_tag", CrmDashboard);
