**BÁO CÁO: THIẾT KẾ CHỨC NĂNG KHẢO SÁT VÀ THU THẬP Ý KIẾN NGƯỜI DÙNG CHO ỨNG DỤNG GỢI Ý DU LỊCH**

**1\. Mục đích xây dựng chức năng khảo sát**

Nhóm xây dựng chức năng khảo sát nhằm thu thập ý kiến và đánh giá của người dùng sau khi trải nghiệm ứng dụng gợi ý du lịch. Thông qua đó, nhóm có thể xác định những ưu điểm, hạn chế của ứng dụng, đánh giá mức độ đáp ứng nhu cầu thực tế và tìm ra những khía cạnh cần cải thiện.

Thay vì yêu cầu người dùng nhập nhận xét tự do dưới dạng văn bản, nhóm lựa chọn hình thức khảo sát bằng các câu hỏi có sẵn đáp án, được thiết kế theo thang điểm từ 1 đến 5. Cách tiếp cận này giúp chuẩn hóa dữ liệu đầu vào, thuận tiện cho việc lưu trữ, thống kê và phân tích kết quả.

**2\. Dữ liệu đầu vào (Input)**

Dữ liệu đầu vào của chức năng khảo sát là các lựa chọn do người dùng cung cấp thông qua việc trả lời những câu hỏi đánh giá có sẵn.

Cụ thể, dữ liệu đầu vào bao gồm:

\- Câu hỏi khảo sát: Được nhóm xây dựng trước, mỗi câu hỏi tập trung đánh giá một tiêu chí cụ thể của ứng dụng hoặc chuyến đi.

\- Các phương án trả lời: Mỗi câu hỏi có 5 phương án được soạn sẵn, tương ứng với 5 mức độ đánh giá từ thấp đến cao.

\- Lựa chọn của người dùng: Người dùng đọc câu hỏi và chọn một trong 5 phương án phù hợp với trải nghiệm của mình.

Ví dụ:

Câu hỏi: Bạn đánh giá giao diện ứng dụng như thế nào?

Các phương án trả lời:

\- 1 điểm: Rất không hài lòng.

\- 2 điểm: Không hài lòng.

\- 3 điểm: Bình thường.

\- 4 điểm: Hài lòng.

\- 5 điểm: Rất hài lòng.

Về mặt kiểu dữ liệu, đây là hình thức dữ liệu lựa chọn có cấu trúc (Structured Data). Người dùng không trực tiếp nhập văn bản hay con số mà lựa chọn một phương án đã được định nghĩa trước. Hệ thống sẽ ghi nhận phương án được chọn dưới dạng giá trị số nguyên (Integer) từ 1 đến 5.

Đây là thang đo thứ bậc (Ordinal Scale), vì các giá trị có thứ tự thể hiện mức độ đánh giá từ thấp đến cao.

**3\. Phương pháp phân loại và xử lý thông tin**

Để thuận tiện cho việc tổng hợp và phân tích dữ liệu, nhóm sử dụng phương pháp gắn thẻ (Tagging) cho các câu hỏi khảo sát, kết hợp với việc mã hóa các phương án trả lời thành điểm số.

3.1. Gắn thẻ cho câu hỏi

Mỗi câu hỏi được gắn một thẻ (Tag) thể hiện nội dung hoặc chủ đề mà câu hỏi đó muốn đánh giá. Các câu hỏi có cùng chủ đề sẽ được xếp vào một nhóm đánh giá chung. Nhờ đó, hệ thống có thể phân loại kết quả và xác định cụ thể từng khía cạnh mà người dùng đang đánh giá.

Nhóm chia thành 3 nhóm chủ đề chính:

\- Nhóm 1 – Trải nghiệm sử dụng ứng dụng: Đánh giá giao diện, tốc độ phản hồi và mức độ thuận tiện khi nhập thông tin.

\- Nhóm 2 – Chất lượng gợi ý của ứng dụng: Đánh giá mức độ phù hợp của địa điểm, cách phân bổ thời gian tham quan, thời gian nghỉ ngơi và độ chính xác của chi phí dự kiến.

\- Nhóm 3 – Mức độ hài lòng của người dùng: Đánh giá sự hài lòng tổng thể, ý định tiếp tục sử dụng và khả năng giới thiệu ứng dụng cho người khác.

Ví dụ về cách gắn thẻ:

\- Câu 1 – Đánh giá giao diện: Tag UI.

\- Câu 2 – Tốc độ phản hồi: Tag Performance.

\- Câu 3 – Nhập thông tin: Tag Input_Usability.

\- Câu 4 – Độ phù hợp địa điểm: Tag Destination.

\- Câu 5 – Phân bổ thời gian tham quan: Tag Schedule.

\- Câu 6 – Thời gian nghỉ ngơi: Tag Rest_Time.

\- Câu 7 – Độ chính xác chi phí: Tag Cost.

\- Câu 8 – Hài lòng tổng thể: Tag Satisfaction.

\- Câu 9 – Tiếp tục sử dụng: Tag Retention.

\- Câu 10 – Giới thiệu ứng dụng: Tag Recommendation.

3.2. Mã hóa câu trả lời thành điểm số

Sau khi người dùng lựa chọn phương án trả lời, hệ thống sẽ ghi nhận điểm số tương ứng từ 1 đến 5.

\- Điểm 1: Mức đánh giá thấp nhất.

\- Điểm 2: Mức đánh giá thấp.

\- Điểm 3: Mức đánh giá trung bình.

\- Điểm 4: Mức đánh giá tốt.

\- Điểm 5: Mức đánh giá cao nhất.

Mỗi câu hỏi có nội dung đáp án riêng phù hợp với tiêu chí đang đánh giá, nhưng đều sử dụng chung thang điểm từ 1 đến 5.

Ví dụ, đối với câu hỏi về tốc độ phản hồi, điểm số tương ứng với mức độ nhanh hay chậm; đối với câu hỏi về sự hài lòng, điểm số tương ứng với mức độ hài lòng của người dùng.

Như vậy, dù nội dung câu trả lời khác nhau, hệ thống vẫn có thể quy đổi về cùng một dạng dữ liệu số để xử lý.

**4\. Quy trình hoạt động của chức năng khảo sát**

Chức năng khảo sát hoạt động theo quy trình sau:

Bước 1: Hiển thị câu hỏi khảo sát.

Hệ thống hiển thị 10 câu hỏi được chia thành 3 nhóm chủ đề, mỗi câu hỏi có 5 phương án trả lời tương ứng với thang điểm từ 1 đến 5.

Bước 2: Người dùng lựa chọn câu trả lời.

Người dùng đọc từng câu hỏi và lựa chọn một phương án phù hợp nhất với trải nghiệm của mình.

Bước 3: Xử lý và phân loại dữ liệu.

Hệ thống ghi nhận phương án được chọn, chuyển đổi thành điểm số tương ứng và liên kết với mã câu hỏi cùng Tag chủ đề.

Bước 4: Lưu trữ kết quả.

Các câu trả lời được lưu thành dữ liệu có cấu trúc để phục vụ quá trình thống kê và phân tích.

Bước 5: Xuất kết quả khảo sát.

Hệ thống tổng hợp kết quả thành tệp dữ liệu để nhóm sử dụng trong việc đánh giá và cải thiện ứng dụng.

**5\. Dữ liệu đầu ra (Output)**

Đầu ra của chức năng là tập dữ liệu chứa các câu trả lời và điểm đánh giá do người dùng cung cấp.

Mỗi lượt khảo sát sẽ ghi nhận các thông tin như:

\- Mã câu hỏi.

\- Tag chủ đề của câu hỏi.

\- Phương án trả lời mà người dùng đã chọn.

\- Điểm số tương ứng từ 1 đến 5.

Ví dụ về dữ liệu đầu ra:

Mã câu hỏi Q1, Tag UI, điểm đánh giá 4.

Mã câu hỏi Q2, Tag Performance, điểm đánh giá 5.

Mã câu hỏi Q3, Tag Input_Usability, điểm đánh giá 3.

Mã câu hỏi Q4, Tag Destination, điểm đánh giá 4.

Mã câu hỏi Q5, Tag Schedule, điểm đánh giá 3.

Mã câu hỏi Q6, Tag Rest_Time, điểm đánh giá 2.

Mã câu hỏi Q7, Tag Cost, điểm đánh giá 4.

Mã câu hỏi Q8, Tag Satisfaction, điểm đánh giá 4.

Mã câu hỏi Q9, Tag Retention, điểm đánh giá 5.

Mã câu hỏi Q10, Tag Recommendation, điểm đánh giá 4.

Kết quả khảo sát có thể được xuất thành tệp CSV hoặc Excel để nhóm dễ dàng lưu trữ, tổng hợp và xử lý dữ liệu.

Từ tập dữ liệu này, nhóm có thể tính điểm trung bình của từng câu hỏi, từng Tag hoặc từng nhóm chủ đề để xác định những khía cạnh được người dùng đánh giá cao và những khía cạnh cần cải thiện.

Ví dụ: Nếu điểm trung bình của Tag Rest_Time thấp, nhóm có thể xem xét điều chỉnh thời gian nghỉ ngơi trong lịch trình được đề xuất.

**6\. Lý do lựa chọn phương pháp khảo sát này**

Nhóm lựa chọn phương pháp khảo sát bằng câu hỏi có sẵn đáp án và thang điểm từ 1 đến 5 vì những lý do sau:

Thứ nhất, dễ dàng thu thập thông tin. Người dùng chỉ cần đọc câu hỏi và lựa chọn đáp án phù hợp, không cần mất thời gian tự viết nhận xét.

Thứ hai, chuẩn hóa dữ liệu đầu vào. Nếu thu thập ý kiến dưới dạng văn bản tự do (Text), mỗi người có thể diễn đạt cùng một ý kiến theo nhiều cách khác nhau. Điều này khiến việc phân loại, thống kê và xử lý dữ liệu trở nên phức tạp hơn.

Thứ ba, thuận tiện cho việc xử lý và phân tích. Các câu trả lời được quy đổi thành điểm số từ 1 đến 5, kết hợp với Tag chủ đề giúp hệ thống dễ dàng phân loại, tính điểm trung bình và so sánh kết quả giữa các tiêu chí.

Thứ tư, hỗ trợ cải thiện ứng dụng dựa trên dữ liệu thực tế. Thông qua kết quả khảo sát, nhóm có thể xác định những tiêu chí đang hoạt động tốt và những tiêu chí chưa đáp ứng mong đợi của người dùng, từ đó đưa ra hướng điều chỉnh phù hợp.

**7\. Kết luận**

Chức năng khảo sát được xây dựng nhằm chuyển đổi ý kiến đánh giá của người dùng thành dữ liệu có cấu trúc, có thể phân loại và xử lý bằng máy tính.

Thông qua việc kết hợp câu hỏi khảo sát, Tag chủ đề và thang điểm từ 1 đến 5, nhóm có thể thu thập ý kiến một cách thống nhất, giảm độ phức tạp trong quá trình xử lý dữ liệu và tạo cơ sở để đánh giá chất lượng ứng dụng.

Kết quả khảo sát không chỉ giúp nhóm biết người dùng hài lòng hay không mà còn hỗ trợ xác định cụ thể những khía cạnh cần cải thiện, góp phần nâng cao chất lượng và mức độ phù hợp của các đề xuất du lịch.