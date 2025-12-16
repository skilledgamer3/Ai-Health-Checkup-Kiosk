import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:flutter_application_1/ai_health_checkup_page.dart';

void main() {
  testWidgets('AiHealthCheckupPage smoke test', (WidgetTester tester) async {
    // Build the widget
    await tester.pumpWidget(const MaterialApp(home: AiHealthCheckupPage()));

    // Verify welcome text
    expect(find.text('Welcome to AI Health Checkup Kiosk'), findsOneWidget);

    // Verify checkbox exists
    expect(find.byType(Checkbox), findsOneWidget);

    // Verify checkbox is initially unchecked
    final checkbox = tester.widget<Checkbox>(find.byType(Checkbox));
    expect(checkbox.value, false);

    // Tap the checkbox
    await tester.tap(find.byType(Checkbox));
    await tester.pump();

    // Verify checkbox is now checked
    final updatedCheckbox = tester.widget<Checkbox>(find.byType(Checkbox));
    expect(updatedCheckbox.value, true);

    // Verify Start Checkup button exists
    expect(find.text('Start Checkup'), findsOneWidget);
  });
}
