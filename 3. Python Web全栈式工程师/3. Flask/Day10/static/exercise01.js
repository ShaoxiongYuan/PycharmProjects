var $prov = $('#prov');
var $city = $('#city');
var $area = $('#area');

$prov.html('<option value=0>请选择</option>');
$city.html('<option value=0>请选择</option>');
$area.html('<option value=0>请选择</option>');

$.each(data, function (index, element) {
    $prov.append('<option value="' + element.provId + '">' + element.provname + '</option>')
});

$prov.on('change', function () {
    $.each(data, function (index, element) {
        if ($prov.val() == element.provId) {
            $city.html('<option value=0>请选择</option>');
            $.each(element.citys, function (i, e) {
                $city.append('<option value="' + e.cityId + '">' + e.cityname + '</option>')
            })
        }
    });

    if ($prov.val() == 0) {
        $city.html('<option value=0>请选择</option>');
    }

    if ($city.val() == 0) {
        $area.html('<option value=0>请选择</option>');
    }
});

$city.on('change', function () {
    $.each(data, function (index, element) {
        if ($prov.val() == element.provId) {
            $.each(element.citys, function (i, e) {
                if ($city.val() == e.cityId) {
                    $area.html('<option value=0>请选择</option>');
                    $.each(e.areas, function (i2, e2) {
                        $area.append('<option value="' + e2.areaId + '">' + e2.areaname + '</option>')
                    })
                }
            })
        }
    })

    if ($city.val() == 0) {
        $area.html('<option value=0>请选择</option>');
    }
});