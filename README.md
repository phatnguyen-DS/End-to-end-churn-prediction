### **Banking Customer Churn**


#### **Mục tiêu**: giảm thiểu rủi ro khách hàng rời bỏ ngân hàng, đảm bảo ứng phó kịp thời trước khi khách hàng có ý định rời đi
#### **Quy trình thực hiện dự án**:
##### Xác định vấn đề và bài toán: 
tình huống: ngân hàng đang có quá nhiều khách hàng rời đi phía nhân viên không phát hiện ra yếu tố tác động tới việc rời bỏ, đồng thời nhân hàng muốn xây dựng một hệ thống Machine Learning dự đoán khách hàng rời bỏ. đồng thời có khả năng mở rộng và triển khai lâu dài, tối ưu hóa, giảm rủi ro cho ngân hàng
#####
Khi nhân viên quản lý khách hàng muốn kiểm tra xem khách hàng mình đang quản lý có khả năng rời bỏ hay không, nhân viên nhập id của khách hàng sau đó hệ thống sẽ trả ra kết quả và mức độ tự tin, giúp phía nhân viên cũng như ngân hàng có thể đưa ra các chính sách ưu đãi, giữ chân khách hàng.
##### phát triển model
###### - Thu thập dữ liệu: nguồn: Kaggle (đã được chuyển đổi để tăng tính thực tế).
###### - Thống kê cơ bản và tìm hiểu dữ liệu: 
###### - Tiền xử lý dữ liệu:
###### - EDA: tìm kiếm insight, đưa ra đề xuất tối ưu dịch vụ.
###### - Nghiên cứu / thử nghiệm tìm ra model và bộ siêu tham số có hiệu quả tốt nhất:
###### - Đánh giá mô hình:

##### Triển khai hệ thống MLops
###### - Kiến trúc hệ thống
###### - Xây dựng hệ thống
###### - Kiểm thử hệ thống

#### **Lưu ý**: vì lượng dữ liệu không đủ nhiều để sử dụng Spark, Deep Learning nên trong dự án này chỉ có thể sử dụng Sklearn và Pandas (có thể phát triển thêm nếu triển khai quy mô lớn)
