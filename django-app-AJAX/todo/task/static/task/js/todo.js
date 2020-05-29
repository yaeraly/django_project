$(document).ready(function() {

	var csrfToken = $("input[name=csrfmiddlewaretoken]").val();

	$('#taskButton').click(function() {
		var serializedData = $('#createTaskForm').serialize();

		$.ajax({
			url: $('#createTaskForm').data('url'),
			data: serializedData,
			type: 'post',
			success: function(response) {
				$('#taskList').append('<div class="card mb-2" id="taskCard" data-id="'+ response.task.id +'" >' +
										'<div class="card-body">'
											+ response.task.title +
											'<button type="button" class="close" aria-label="Close" data-id="'+response.task.id+'">' +
		          								'<span aria-hidden="true">&times;</span>' +
		        							'</button>' +
										'</div>' +
									'</div>'
				)
			}
		});

		$('#createTaskForm')[0].reset();
	});

	$('#taskList').on('click', '.card', function() {
		var dataId = $(this).data('id');

		$.ajax({
			url: '/task/'+ dataId + '/completed/',
			data: {
				csrfmiddlewaretoken: csrfToken,
				pk: dataId,
			},
			type: 'post',
			success: function() {
				var cardItem = $('#taskCard[data-id="' + dataId + '"]');
				cardItem.css('text-decoration', 'line-through').hide().slideDown();
				$('#taskList').append(cardItem);
			}
		});
		
	}).on('click', 'button.close', function(event) {
		event.stopPropagation();

		var dataId = $(this).data('id');

		$.ajax({
			url: '/task/' + dataId + '/delete/',
			data: {
				csrfmiddlewaretoken: csrfToken,
				pk: dataId,
			},
			type: 'post',
			dataType: 'json',
			success: function() {
				$('#taskCard[data-id=' + dataId + ']').remove();
			}
		});
	});

});
