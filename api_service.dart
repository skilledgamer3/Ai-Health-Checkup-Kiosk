import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  final String baseUrl;

  ApiService(this.baseUrl);

  Future<Map<String, dynamic>> predictDisease(
    Map<String, dynamic> payload, {
    String model = "rf",
  }) async {
    final url = Uri.parse("$baseUrl/predict?model=$model");

    final response = await http.post(
      url,
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(payload),
    );

    if (response.statusCode != 200) {
      throw Exception("API Error: ${response.body}");
    }

    return jsonDecode(response.body);
  }
}
