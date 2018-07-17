$(document).ready(function() {
    blindioSettingsLoad();
});

var blindio_pacs_server_setting_ids = [
    "blindio__settings_pacs_server_aetitle",
    "blindio__settings_pacs_server_host",
    "blindio__settings_pacs_server_port"
];

var blindio_pacs_client_setting_ids = [
    "blindio__settings_pacs_client_aetitle",
    "blindio__settings_pacs_client_port"
];

var blindio_pacs_setting_ids = blindio_pacs_server_setting_ids.concat(blindio_pacs_client_setting_ids);


function blindioSettingsLoad() {
    blindio_pacs_setting_ids.forEach(function(item, i, arr) {
        blindioSettingLoad(item);
    });
};

function blindioSavePacsServerSetting() {
    // TODO save all settings in group by one request
    // TODO show success message when all saved done
    blindio_pacs_server_setting_ids.forEach(function(item, i, arr) {
        input_tag_id = "#" + item + "__input";
        value = $(input_tag_id).val();
        label_tag_id = "#" + item + "__label";
        label = $(label_tag_id).text();
        blindioSettingSave(item, label, value);
    });
};

function blindioSavePacsClientSetting() {
    // TODO save all settings in group by one request
    // TODO show success message when all saved done
    blindio_pacs_client_setting_ids.forEach(function(item, i, arr) {
        input_tag_id = "#" + item + "__input";
        value = $(input_tag_id).val();
        label_tag_id = "#" + item + "__label";
        label = $(label_tag_id).text();
        blindioSettingSave(item, label, value);
    });
};

function blindioSettingLoad(setting_id) {
    $.ajax({
        "method": "GET",
        "url": window.location.origin + "/settings/" + setting_id + "/",
        "dataType": "json"
    }).done(function(json) {
        $("#" + json.name + "__input").val(json.value);
    });
};

function blindioSettingSave(setting_id, setting_label, setting_value) {
    $.post(window.location.origin + "/settings/" + setting_id + "/",
    {
        "name": setting_id,
        "label": setting_label,
        "value": setting_value
    });
};